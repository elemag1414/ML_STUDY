import tensorflow as tf
from glob import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import io

image_path = 'dataset/images/'
label_path = 'dataset/labels/'

# Transform config
resize = True
num_epoch = 2
shuffle = True


def _resize_function(image_decoded, label):
    image_decoded.set_shape([None, None, None])
    image_resized = tf.image.resize_images(image_decoded, [100, 100])
    return image_resized, label


def read_image(path):
    image = np.array(Image.open(path))
    return image


def get_list(im_path, label_path):
    image_list = glob(im_path + '*.*')
    label_list = glob(label_path + '*.*')
    a = [label.split('.')[0] for label in label_list]
    label = [_a.split('/')[2] for _a in a]
    label = np.array(label).astype(np.uint8)
    print('label list: {}'.format(label))
    return image_list, label


def generator(path, label_list):
    for im, label in zip(path, label_list):
        image = read_image(im)
        yield image.astype(np.int32), label
    # image = cv2.imread(path)


def main():
    batch_size = 2

    image_list, label_list = get_list(image_path, label_path)

    dataset = tf.data.Dataset.from_generator(generator=generator,
                                             output_types=(
                                                 tf.int32, tf.uint8),
                                             output_shapes=(tf.TensorShape([None, None, None]),
                                                            tf.TensorShape([])),
                                             args=[image_list, label_list])

    if resize:
        # Note just "dataset.map(_resize_function)" will not be excuted
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

    cnt = 0
    with tf.Session() as sess:

        sess.run(iterator.initializer)
        while True:
            cnt += 1
            try:
                image, label = sess.run([image_stacked, label_stacked])
                print('[{}]: {} image.shape{}   {} {} {}'.format(
                    cnt, label, tf.shape(image), image.shape[0], image.shape[1], image.shape[2]))

                image = image.astype(int)  # Convert to integer type
                jpeg_image = np.squeeze(image)
                # jpeg_image = image
                print('[batch:{}] label: {} (#lables: {})'.format(
                    cnt, label, label.size))

                # plt.imshow(jpeg_image)
                # plt.show()

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
