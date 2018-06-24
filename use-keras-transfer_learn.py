import os ,os.path
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model, load_model
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Suppress warning and informational messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
inputDir = "naga"
clasificationList =['Daisy','Dandelion']

new_model = load_model('inceptionv3-transfer-learning.model')

for root, dirs, files in os.walk(inputDir):
    for filename in files:

        img = image.load_img(inputDir+'/'+filename, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)
        x = preprocess_input(x)
        
        features = new_model.predict(x)
        print('****************************************')
        print(" ")
        print('Processing file : '+ filename)
        print('Here are the weights : ',features)
        display_img=mpimg.imread(inputDir+'/'+filename)
        imgplot = plt.imshow(display_img)
        if features[0][0] > features[0][1] :
            print('Input image clasification is : '+clasificationList[0])
        else:
            print('Input image clasification is : '+clasificationList[1])
        print(" ")

print('****************************************')
# https://www.youtube.com/watch?v=osaKmG5i30E