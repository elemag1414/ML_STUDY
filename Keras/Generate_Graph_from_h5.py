from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from keras import backend as K
import tensorflow as tf
from keras.models import load_model

import argparse
import sys
import os

from tensorflow.core.framework import graph_pb2
from tensorflow.python.client import session
from tensorflow.python.framework import importer
from tensorflow.python.framework import ops
from tensorflow.python.platform import app
from tensorflow.python.platform import gfile
from tensorflow.python.summary import summary


# freeze h5 model
def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(
            set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = tf.graph_util.convert_variables_to_constants(
            session, input_graph_def, output_names, freeze_var_names)
        return frozen_graph


# # Generate Graph from pb file
try:
    from tensorflow.contrib.tensorrt.ops.gen_trt_engine_op import *
except ImportError:
    pass


def import_to_tensorboard(model_dir, log_dir):
    # This method is copied from
    # from tensorflow/tensorflow/python/tools/import_pb_to_tensorboard.py
    with session.Session(graph=ops.Graph()) as sess:
        with gfile.GFile(model_dir, "rb") as f:
            graph_def = graph_pb2.GraphDef()
            graph_def.ParseFromString(f.read())
            importer.import_graph_def(graph_def)

        pb_visual_writer = summary.FileWriter(log_dir)
        pb_visual_writer.add_graph(sess.graph)
        print("Model Imported. Visualize by running: "
              "tensorboard --logdir={}".format(log_dir))


def main(unused_args):
    # 1. Convert h5 to pb
    # Create, compile and train model...
    model = load_model(FLAGS.model_dir)

    frozen_graph = freeze_session(K.get_session(),
                                  output_names=[out.op.name for out in model.outputs])

    tmp_pb_file = 'tmp_my_model.pb'
    tf.train.write_graph(frozen_graph, "./",
                         tmp_pb_file, as_text=False)

    # 2. Generate Graph from pb
    import_to_tensorboard(tmp_pb_file, FLAGS.log_dir)

    # 3. remove temporary pb file
    os.remove(tmp_pb_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
        "--model_dir",
        type=str,
        default="",
        required=True,
        help="The location of the protobuf (\'pb\') model to visualize.")
    parser.add_argument(
        "--log_dir",
        type=str,
        default="",
        required=True,
        help="The location for the Tensorboard log to begin visualization from.")
    FLAGS, unparsed = parser.parse_known_args()
    app.run(main=main, argv=[sys.argv[0]] + unparsed)
