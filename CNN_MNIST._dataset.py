# -*- coding: utf-8 -*-
"""CNN_mnist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11eqWMXCDkkwfb5hVJShbt5TRjie86zK-
"""

from tensorflow.keras.datasets import mnist
import tensorflow as tf
from skimage.transform import resize
from skimage.io import imread

# Loading Data
(x_train,y_train),(x_test,y_test)=mnist.load_data()

y_test

x_train.shape

y_train.shape

x_test.shape

import matplotlib.pyplot as plt
plt.imshow(x_train[0])

# Reshape the data
x_train=x_train.reshape(60000,28,28,1)
x_test=x_test.reshape(10000,28,28,1)
x_train.shape

# Normalize the pixel value
x_train=x_train/255.0
x_test=x_test/255.0

# Model Creation
model=tf.keras.models.Sequential([
    # Feature Exteraction
    tf.keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation='relu',input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

    # Fully connected layer
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=128,activation='relu'),
    tf.keras.layers.Dense(units=10,activation='softmax')
])

# compilation
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=6000,epochs=10)

loss,accuracy=model.evaluate(x_test,y_test)

# reshaping of new image
img_path='/content/mnist1.png'
img=imread(img_path)
resized_image=resize(img,(28,28,1))
reshaped_image=resize(img,(1,28,28,1))

# predicting image
prediction=model.predict(reshaped_image)
prediction

ind=prediction.argmax()
ind

# image_index = i  # Change this to the index of the image you want to display
plt.imshow(resized_image)  # Use x_test to display the actual image data
# plt.title(f"True Label: {y_test[image_index]}")  # Optionally display the true label as a title
# plt.show()
# print(reshaped_image.shape)
# print(x_train.shape)

# Assuming x_test contains your image data
for i in range(1,10):
  plt.subplot(10,1,i)
  image_index = i  # Change this to the index of the image you want to display
  plt.imshow(x_test[image_index])  # Use x_test to display the actual image data
  print(x_test[image_index].shape)
  plt.title(f"True Label: {y_test[image_index]}")  # Optionally display the true label as a title
  plt.show()



model.save("mnist_CNN_model.h5")
