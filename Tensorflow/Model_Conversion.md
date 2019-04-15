# Trained Model 변환하기

## Convert Keras Model (h5) to Tensorflow Model (ckpt)

```python
# Add ops to save and restore all the variables.
import keras
saver = tf.train.Saver()
model = keras.models.load_model("model.h5")
sess = keras.backend.get_session()
save_path = saver.save(sess, "/path/to_ckpt/model.ckpt")
```

> [출처: Stack overflow](https://github.com/keras-team/keras/issues/9040) <br><br>

## Convert Keras Model (h5) to Tensorflow Model (pb format)

pb format으로 변환하는 방법은 ckpt로 변환하는 방법과 유사하지만,
pb format으로 변환하기 위해서는 export하기 위한 freeze과정을 거쳐야 한다.

이를 위해 다음의 freeze_session() 유틸리티 method를 사용한다.

```python
def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    """
    Freezes the state of a session into a pruned computation graph.

    Creates a new computation graph where variable nodes are replaced by
    constants taking their current value in the session. The new graph will be
    pruned so subgraphs that are not necessary to compute the requested
    outputs are removed.
    @param session The TensorFlow session to be frozen.
    @param keep_var_names A list of variable names that should not be frozen,
                          or None to freeze all the variables in the graph.
    @param output_names Names of the relevant graph outputs.
    @param clear_devices Remove the device directives from the graph for better portability.
    @return The frozen graph definition.
    """
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = tf.graph_util.convert_variables_to_constants(
            session, input_graph_def, output_names, freeze_var_names)
        return frozen_graph
```

여기서,

> freeze_session()의
>
> > session: TF session object
> > keep_var_names: 일부 varable이 frozen (예를 들어 stateful 모델)되지 않기를 원한다면 True설정.
> > output_names: output으로 생성되기를 바라는 operation의 이름들을 element로 갖는 list.
> > clear_devices: graph를 좀 더 portable하게 생성하기 위해 device directives를 제거 할때 True로 설정.

이후, Keras 모델 model을 freeze_session()을 이용하여 tensorflow graph (frozen_graph)로 생성해준다.

```python
from keras import backend as K

# Create, compile and train model...

frozen_graph = freeze_session(K.get_session(),
                              output_names=[out.op.name for out in model.outputs])
```

frozen_graph는 tensorflow graph 이며,
이제 tf.train.write_graph()를 사용하여 pb format으로 저장해준다.

```python
tf.train.write_graph(frozen_graph, "some_directory", "my_model.pb", as_text=False)
```

> [출처: Stack overflow](https://stackoverflow.com/questions/45466020/how-to-export-keras-h5-to-tensorflow-pb) <br><br>

## Convert Tensorflow model to Keras model

To be added <br><br>

##### [[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[Keras로 돌아기기]](https://github.com/elemag1414/Keras)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
