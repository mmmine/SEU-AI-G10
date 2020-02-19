import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
import MyUtil

def BuildConvModel():
	My_model = Sequential()

	My_model.add(Conv2D(filters = 32, kernel_size = (5, 5), padding = 'Same', activation = 'relu',input_shape = (28,28,1)))
	My_model.add(Conv2D(filters = 64, kernel_size = (3, 3), padding = 'Same', activation = 'relu'))
	My_model.add(MaxPooling2D(pool_size = (2, 2)))
	My_model.add(Dropout(0.2))
	My_model.add(Conv2D(filters = 64, kernel_size = (3, 3), padding = 'Same', activation = 'relu'))
	My_model.add(Conv2D(filters = 64, kernel_size = (3, 3), padding = 'Same', activation = 'relu'))
	My_model.add(MaxPooling2D(pool_size = (2, 2)))
	My_model.add(Dropout(0.2))
	My_model.add(Flatten())
	My_model.add(Dense(512, activation = 'relu'))
	My_model.add(Dropout(0.1))
	My_model.add(Dense(10, activation = 'softmax'))

	My_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
	return My_model


def ProcessDataWithConv2D(images, label):
	images = MyUtil.ProcessImagesWithConv2D(images)
	label = MyUtil.ProcessLabel(label)
	return (images, label)

