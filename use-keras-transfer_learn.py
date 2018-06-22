import os

from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model
from keras.models import load_model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from keras.preprocessing import image

# Suppress warning and informational messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

new_model = load_model('inceptionv3-transfer-learning.h5')

# new_model.summary()
# new_model.get_weights()
# new_model.optimizer

"""
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
print('predictions {0}'.format(predictions))
# print('predictions {0}'.predictions)
#   Connect the image generator to a folder contains the source images the image generator alters.  
#   Training image generator
# train_generator = train_image_gen.flow_from_directory(
#   train_dir,
#   target_size=(Image_width, Image_height),
#   batch_size=batch_size
# )
"""
img_path = 'test-images/daisy/Daisy1.jpg'

img = image.load_img(img_path, target_size=(299, 299))
x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)
x = preprocess_input(x)

features = model.predict(x)
print(decode_predictions(features, top = 2))


"""
https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
https://github.com/fchollet/deep-learning-with-python-notebooks
https://www.learnopencv.com/keras-tutorial-fine-tuning-using-pre-trained-models/

from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.applications.inception_v3 import decode_predictions

from keras.preprocessing import image

import numpy as np
import matplotlib.pyplot as plt
#--------------------------------

store_model = False

#--------------------------------

if store_model == True:
	model = InceptionV3(weights='imagenet', include_top=True)
	
	#save model and weights
	model_config = model.to_json()
	open("inceptionv3_structure.json", "w").write(model_config)
	model.save_weights('inceptionv3_weights.h5')
else:
	from keras.models import model_from_json
	model = model_from_json(open("inceptionv3_structure.json", "r").read())
	model.load_weights('inceptionv3_weights.h5')
	print("inception v3 model loaded")
	
#print("model structure: ", model.summary())
#print("model weights: ", model.get_weights())

#put images in testset folder, name images from 1.jpg to 16.jpg
for i in range(1, 17):
	
	img_path = 'testset/%s.jpg' % (i)
	
	img = image.load_img(img_path, target_size=(299, 299))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis = 0)
	x = preprocess_input(x)
	
	features = model.predict(x)
	print(decode_predictions(features, top = 3))
	
	plt.imshow(image.load_img(img_path))
	plt.show()

"""