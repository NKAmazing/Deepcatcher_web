import tensorflow as tf

print("Versión TensorFlow:", tf.__version__)
print("Num GPUs disponibles:", len(tf.config.list_physical_devices('GPU')))
print("Nombre de GPU:", tf.config.list_physical_devices('GPU'))
print("Dispositivos totales:", tf.config.list_physical_devices())
print("Cuda version:", tf.sysconfig.get_build_info()['cuda_version'])
print("Cudnn version:", tf.sysconfig.get_build_info()['cudnn_version'])