import tensorflow as tf
from glob import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = 'dataset/images/'
label_path = 'dataset/labels/'

# Transform config
resize = True
num_epoch = 1   # 0 for repeat forever
shuffle = True
batch_size = 2


def read_image(path):
    image = np.array(Image.open(path))
    return image


def _read_py_function(path, label):
    image = read_image(path)
    # image = cv2.imread(path)
    return image.astype(np.int32), label


def _resize_function(image_decoded, label):
    image_decoded.set_shape([None, None, None])
    image_resized = tf.image.resize_images(image_decoded, [100, 100])
    return image_resized, label


def get_list(im_path, label_path):
    image_list = glob(im_path + '*.*')
    label_list = glob(label_path + '*.*')
    a = [label.split('.')[0] for label in label_list]
    label = [_a.split('/')[2] for _a in a]
    label = np.array(label).astype(np.uint8)
    return image_list, label


def main():
    image_list, label_list = get_list(image_path, label_path)
    print('Image List: {}'.format(image_list))
    print('Label List: {}'.format(label_list))

    # Create tf.data.Dataset Instance
    dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))

    # Feed in custom generator via tf.py_func()
    dataset = dataset.map(
        lambda image_list, label_list: tuple(tf.py_func(_read_py_function, [image_list, label_list], [tf.int32, tf.uint8])))

    if resize:
        dataset = dataset.map(_resize_function)

    if num_epoch == 0:
        dataset = dataset.repeat()  # repeat forever
    else:
        dataset = dataset.repeat(num_epoch)

    if shuffle:
        dataset = dataset.shuffle(buffer_size=(
            int(len(image_list) * 0.4) + 3 * batch_size))

    # transform tf.data.Dataset Instance
    dataset = dataset.batch(batch_size)

    # Create Iterator
    iterator = dataset.make_initializable_iterator()
    image_stacked, label_stacked = iterator.get_next()

    with tf.Session() as sess:

        sess.run(iterator.initializer)
        while True:
            try:
                image, label = sess.run([image_stacked, label_stacked])

                image = image.astype(int)  # Convert to integer type
                jpeg_image = np.squeeze(image)

                # display image for debug
                for im in jpeg_image:
                    plt.imshow(im)
                    plt.show()

            except tf.errors.OutOfRangeError:
                print("End of training dataset.")
                break


if __name__ == "__main__":
    main()
