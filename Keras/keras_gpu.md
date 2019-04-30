# Tensorflow, Keras가 GPU 사용하는지 확인하기

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

## How to check if Keras is using GPU

```python
from keras import backend as K
K.tensorflow_backend._get_available_gpus()

['/gpu:0']
```
