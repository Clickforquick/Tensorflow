FROM python:3.6.3

RUN pip install --upgrade pip

# Install tensorflow
RUN pip install --upgrade \
  https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.7.1-cp36-cp36m-linux_x86_64.whl

# tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl
# tensorflow-1.7.0-cp35-cp35m-manylinux1_x86_64.whl
# Install dependencies
RUN pip install --upgrade numpy
RUN pip install --upgrade pandas
RUN pip install --upgrade matplotlib
RUN pip install --upgrade tensorflow_hub
# RUN pip install --upgrade matplotlib

# Create app directory
WORKDIR /usr/src/app

# Bundle app source
COPY . .

# CMD [ "python", "retrain.py" ]

CMD [ "python", "SimpleMNIST.py" ]

# CMD [ "python", "House_Price_Prediction.py" ]
