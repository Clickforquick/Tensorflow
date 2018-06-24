## Dependencies
 Python >=3
 Pip
 Tensorflow -> pip install tensorflow==1.5
 Jupyter notebook -> pip install jupyter
 Keras -> pip install keras
 numpy -> pip install numpy

## Project Setup

 # Overview:
        This project is an demo of using Transfer Learning.  Transfer learning let apply the power of an existing powerful trained model to a dataset we are interested in. In this example, we will use the Inveption-V3 model along with Keras to perform image classification. This project can be used to classifiy any catgory of images provided we have trained the algorithm using images of that category. Though there is no limit on number of image categories we can train and classifiy using this algorithm, we have trained, validated and tested the algorithm using only 2 classes of images "daisy" and "dandelion".

# Process to run the existing project and classifiy "daisy" and "dandelion" flowers
 1. Install the dependencies.
 2. Clone or download the current project.
 3. Move to root folder and open command prompt.
 4. Run jupyter notebook (Jupyter notebook will open entire project solution in a web browser)
 5. Select Keran-transfer_learn.ipynb and execute the blocks.Here we are training the algorithm and this proecess will be run for a considerable amount of time depending on system hardware configuration.
 6. Once training is complete we will see a file named inceptionv3-fine-tune.h5 in root folder
 7. Now select use-keras-transfer_learn.ipynb from jupyter notebook and run the code blocks.
 8. At the end we will the test images and their classification

# Process to train and classify images of different categories
  1.Delete "data" and "test" folders in root folder (Tensorflow)
  2.Create a folder named data.  Under that folder create the subfolders "train" and "validate" 
  3.create subfolders for each category of images in both "train" and "validate" folders
  4.Place training images in subfolders under "train" folder
  5.Place validation images in subfolders under "validate" folder
  6.Create a folder named "test" under "data" folder.
  7.copy images to be classified under test folder
  8.Open "use-keras-transfer_learn.ipynb" in jupyter notebook
  9.modify "clasificationList =['Daisy','Dandelion']" code block
  10.Replace ['Daisy','Dandelion'] with the classes used in above training process and save the file.Class names are the names of    folders containg the images
   11.Repeat the steps from 3-8 from "Process to run existing project"
