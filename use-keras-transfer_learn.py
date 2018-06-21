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

# new_model.summary()
# new_model.get_weights()
# new_model.optimizer


def create_img_generator():
  return  ImageDataGenerator(
      preprocessing_function=preprocess_input
  )


# Main Code
Image_width, Image_height = 299, 299 
test_dir = './test-images'
# Batch_Size = 32
test_batches = ImageDataGenerator().flow_from_directory(test_dir,target_size=(299,299),classes=['daisy','dandelion'],batch_size=10)

predictions = new_model.predict_generator(test_batches,steps=1,verbose=0)
predictions
#   Connect the image generator to a folder contains the source images the image generator alters.  
#   Training image generator
# train_generator = train_image_gen.flow_from_directory(
#   train_dir,
#   target_size=(Image_width, Image_height),
#   batch_size=batch_size
# )
