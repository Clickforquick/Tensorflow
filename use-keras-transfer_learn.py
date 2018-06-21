import os

from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model
from keras.models import load_model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD

# Suppress warning and informational messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

new_model = load_model('inceptionv3-transfer-learning.h5')

new_model.summry()
new_model.get_weights()
new_model.optimizer
