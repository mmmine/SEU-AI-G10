import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import MyUtil

def BuildDenseModel():
	My_model = Sequential()
	My_model.add(Dense(512, activation = 'relu', input_shape = (784, )))
	My_model.add(Dense(256, activation = 'relu'))
	My_model.add(Dense(10, activation = 'softmax'))
	My_model.compile(optimizer = SGD(), loss = 'categorical_crossentropy', metrics = ['accuracy'])
	return My_model

def ProcessDataWithDense(images, label):
	images = MyUtil.ProcessImagesWithDense(images)
	label = MyUtil.ProcessLabel(label)
	return (images, label)


