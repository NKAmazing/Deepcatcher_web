import tensorflow as tf

print("Versión TensorFlow:", tf.__version__)
print("Num GPUs disponibles:", len(tf.config.list_physical_devices('GPU')))
print("Dispositivos:", tf.config.list_physical_devices())