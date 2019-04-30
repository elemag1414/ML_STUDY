# Tensorflow, Keras가 GPU 사용하는지 확인하기

---

## How to check if the code is running on GPU or CPU

```python
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())


[name: "/cpu:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 4800764240957379342
, name: "/gpu:0"
device_type: "GPU"
memory_limit: 6814913823
locality {
  bus_id: 1
}
incarnation: 14858485129082007400
physical_device_desc: "device: 0, name: GeForce GTX 1070, pci bus id: 0000:01:00.0"
]
```

---

## Tensorflow에서 확인

### How to check if Tensorflow is using GPU

```python
import tensorflow as tf

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
```

다음과 같은 output이 출력되는지 확인:

```python
I tensorflow/core/common_runtime/gpu/gpu_device.cc:885] Found device 0 with properties:
name: GeForce GT 730
major: 3 minor: 5 memoryClockRate (GHz) 0.9015
pciBusID 0000:01:00.0
Total memory: 1.98GiB
Free memory: 1.72GiB
I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0
I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GT 730, pci bus id: 0000:01:00.0)
Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GeForce GT 730, pci bus id: 0000:01:00.0
I tensorflow/core/common_runtime/direct_session.cc:255] Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GeForce GT 730, pci bus id: 0000:01:00.0
```

### Helper function사용하기

- [tf.test.is_gpu_available](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available) tells if the gpu is available
- [tf.test.gpu_device_name](https://www.tensorflow.org/api_docs/python/tf/test/gpu_device_name) returns the name of the gpu device

다음과 같이 `sess.list_devices()`를 사용하여 확인할 수 있다:

```python
with tf.Session() as sess:
  devices = sess.list_devices()
```

상기 snippet을 실행하면 `devices`로 다음과 같은 것들이 반환된다:

```python
[_DeviceAttributes(/job:tpu_worker/replica:0/task:0/device:CPU:0, CPU, -1, 4670268618893924978),
 _DeviceAttributes(/job:tpu_worker/replica:0/task:0/device:XLA_CPU:0, XLA_CPU, 17179869184, 6127825144471676437),
 _DeviceAttributes(/job:tpu_worker/replica:0/task:0/device:XLA_GPU:0, XLA_GPU, 17179869184, 16148453971365832732),
 _DeviceAttributes(/job:tpu_worker/replica:0/task:0/device:TPU:0, TPU, 17179869184, 10003582050679337480),
 _DeviceAttributes(/job:tpu_worker/replica:0/task:0/device:TPU:1, TPU, 17179869184, 5678397037036584928)
```

---

## Keras에서 확인

### How to check if Keras is using GPU

```python
from keras import backend as K
K.tensorflow_backend._get_available_gpus()

['/gpu:0']
```

##### [[Keras로 돌아가기]](README.md) | [[Tensorflow로 돌아가기]](../Tensorflow/README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
