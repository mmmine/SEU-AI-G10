import numpy as np
import keras
from keras import backend as K
from keras.utils import np_utils
from keras.models import Model
from keras.layers import Dense,Input,Convolution2D,Flatten,add,Activation,AveragePooling2D
from keras.optimizers import Adam
from keras.utils import plot_model

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


#Resnet模型定义
def res_block(net, channels, i):
    if i == 1:
        strides = (1, 1)
        net_bottleneck = net
    else:
        strides = (2, 2)
        net_bottleneck = Convolution2D(channels,
                                       kernel_size=(3, 3),
                                       activation='relu',
                                       padding='same',
                                       strides=strides)(net)

    net = Convolution2D(channels,
               kernel_size=(3, 3),
               activation='relu',
               padding='same')(net)
    net = Convolution2D(channels,
               kernel_size=(3, 3),
               padding='same',
               strides=strides)(net)

    net = add([net, net_bottleneck])
    Activation(K.relu)(net)
    return net

inputnet=Input(shape=(28, 28, 1))

net = Convolution2D(
        input_shape=(28, 28, 1),
        filters=16,
        kernel_size=3,
        padding='same',
        activation='relu'
)(inputnet)

for i in range(2):
    net=res_block(net, 16, i)

for i in range(2):
    net=res_block(net, 32, i)

net=AveragePooling2D(pool_size=(7, 7))(net)
net=Flatten()(net)
net=Dense(10, activation='softmax')(net)

model = Model(input=inputnet,outputs = net)
adam = Adam(lr=1e-4)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(x_train, y_train, batch_size=128, epochs=10,validation_data=(x_test, y_test))

# 评估模型
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print('test loss', test_loss)
print('test accuracy', test_accuracy)


