import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Convolution2D,MaxPooling2D,Flatten
from keras.optimizers import Adam


#导入MNIST数据集
path='./mnist.npz'
f = np.load(path)
x_train, y_train = f['x_train'], f['y_train']
x_test, y_test = f['x_test'], f['y_test']
f.close()


#数据处理
x_train = x_train.reshape(-1,28,28,1)/255.0
x_test = x_test.reshape(-1,28,28,1)/255.0
y_train = np_utils.to_categorical(y_train,num_classes=10)
y_test = np_utils.to_categorical(y_test,num_classes=10)


# CNN模型定义
model = Sequential()

model.add(Convolution2D(
    input_shape=(28, 28, 1),
    filters=64,
    kernel_size=5,
    strides=1,
    padding='same',
    activation='relu'
))

model.add(MaxPooling2D(
    pool_size=2,
    strides=2,
    padding='same',
))

model.add(Convolution2D(
    filters=64,
    kernel_size=5,
    strides=1,
    padding='same',
    activation='relu'
))

model.add(MaxPooling2D(
    pool_size=2,
    strides=2,
    padding='same',
))

model.add(Flatten())
model.add(Dense(1024,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))
adam = Adam(lr=1e-4)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(x_train, y_train, batch_size=64, epochs=10)

# 评估模型
test_loss,test_accuracy = model.evaluate(x_test, y_test)
print('test loss', test_loss)
print('test accuracy', test_accuracy)
