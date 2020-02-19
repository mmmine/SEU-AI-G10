import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D, GlobalMaxPooling2D
from keras.datasets import cifar10
import matplotlib.pyplot as plt

def build_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32,32,3))) #卷积层
    model.add(Activation('relu')) #激活函数
    model.add(MaxPooling2D(pool_size=(2, 2))) #池化
    #重复三次
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten()) #全连接层
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))

    #编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

(x_train, y_train), (x_val, y_val) = cifar10.load_data() #载入数据，已预下载
y_train = keras.utils.to_categorical(y_train, 10)
y_val = keras.utils.to_categorical(y_val, 10) #十分类
x_train = x_train.astype('float32')
x_val = x_val.astype('float32')
x_train /= 255
x_val /= 255

model = build_model()

#fit方法返回History对象
hist = model.fit(x_train, y_train, batch_size=64, epochs=50, validation_data=(x_val, y_val))
print(model.summary()) #显示模型摘要

model.save('./model/deepmodel_cifar10.hdf5') 
model.save_weights('./model/deepmodel_cifar10_weight.hdf5')

#History对象的history属性记录了损失函数和精确度等指标随epoch的变化情况
hist_dict = hist.history
print("train acc:", hist_dict['acc'])
print("validation acc:", hist_dict['val_acc'])

#绘图显示训练过程各指标变化情况
def show_train_history(train_hist, train, validation):
    plt.plot(train_hist[train])
    plt.plot(train_hist[validation])
    plt.ylabel(train)
    plt.xlabel('epoch')
    plt.legend(['train','validation'], loc='upper left')
    plt.show()
show_train_history(hist_dict, 'acc', 'val_acc')
show_train_history(hist_dict, 'loss', 'val_loss')

#评估模型
score = model.evaluate(x_val, y_val)
print(score[1])