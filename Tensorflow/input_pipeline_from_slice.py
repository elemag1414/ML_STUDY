import tensorflow as tf
from glob import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# import io

image_path = 'dataset/images/'
label_path = 'dataset/labels/'

# Transform config
resize = True
num_epoch = 1
shuffle = True

#NUM_CLASSES = 10
# def input_parser(img_path, label):
#     print('[input_parser] img_path: {}'.format(img_path))
#     print('[label] label: {}'.format(label))
#     # convert the label to one-hot encoding
#     one_hot = tf.one_hot(label, NUM_CLASSES)

#     # read the img from file
#     img_file = tf.read_file(img_path)
#     img_decoded = tf.image.decode_image(img_file, channels=3)
#     img_decoded.set_shape([None, None, None])
#     # img_decoded = tf.image.resize_images(img_decoded, [28, 28])
#     img_decoded = tf.image.resize_images(img_decoded, [100, 100])
#     return img_decoded, one_hot


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
    print('label list: {}'.format(label))
    return image_list, label


def main():
    image_list, label_list = get_list(image_path, label_path)
    print('Image List: {}'.format(image_list))
    print('Label List: {}'.format(label_list))

    dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))

    batch_size = 2

    dataset = dataset.map(
        lambda image_list, label_list: tuple(tf.py_func(_read_py_function, [image_list, label_list], [tf.int32, tf.uint8])))

    if resize:
        dataset = dataset.map(_resize_function)

    if num_epoch == 0:
        print('# epoch: Indefinite')
        dataset = dataset.repeat()
    else:
        print('# epoch: {}'.format(num_epoch))
        dataset = dataset.repeat(num_epoch)

    if shuffle:
        dataset = dataset.shuffle(buffer_size=(
            int(len(image_list) * 0.4) + 3 * batch_size))

    dataset = dataset.batch(batch_size)

    # Iterator Set up
    iterator = dataset.make_initializable_iterator()
    image_stacked, label_stacked = iterator.get_next()
    print('image_stacked.shape: {}'.format(image_stacked.shape))
    print('label_stacked.shape: {}'.format(label_stacked.shape))

    cnt = 0
    with tf.Session() as sess:

        sess.run(iterator.initializer)
        while True:
            # sess.run(iterator.initializer)
            cnt += 1
            try:
                image, label = sess.run([image_stacked, label_stacked])
                # print('[{}]: {}'.format(cnt, tf.shape(image)))

                image = image.astype(int)  # Convert to integer type
                jpeg_image = np.squeeze(image)
                print('[batch:{}] label: {} (#lables: {})'.format(
                    cnt, label, len(label)))

                for im in jpeg_image:
                    print('Image Size: {}x{}'.format(im.shape[0], im.shape[1]))
                    plt.imshow(im)
                    plt.show()

                print('{}th batch job done...'.format(cnt))

            except tf.errors.OutOfRangeError:
                print("End of training dataset.")
                break


if __name__ == "__main__":
    main()
