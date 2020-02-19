import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.datasets.mnist as mnist
import tensorflow.keras.layers as layers
import numpy as np

# 优化器
from tensorflow.keras.optimizers import SGD

### 准备数据 
# (((60000, 28, 28), (60000,)), ((10000, 28, 28), (10000,)))
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

x_train = np.array(x_train, dtype=np.float32)
x_test = np.array(x_test, dtype=np.float32)

# 将数字转换成one-hot向量
def num_to_onehot(list):
    y = np.zeros(shape=(list.shape[0], 10))
    for i in range(list.shape[0]):
        y[i, list[i]] = 1
    return y

y_train = num_to_onehot(y_train)  
y_test = num_to_onehot(y_test)

### 定义神经网络

# 1. 层定义
# 输入层
x = keras.Input(shape=(28, 28, 1), dtype=tf.float32)  # shape是图片的shape， 与数量无关

# 卷积层
con1 = layers.Conv2D(filters=6,
                    kernel_size=(5, 5),
                    strides=(1,1),
                    padding="same",
                    activation="relu",
                    dtype=tf.float32)

# strides默认为pool_size
pool1 = layers.AveragePooling2D(pool_size=(2,2), strides=(2,2), padding="same")

con2 = layers.Conv2D(filters=16,
                    kernel_size=(5, 5),
                    strides=(1,1),
                    padding="valid",
                    activation="relu",
                    dtype=tf.float32)

pool2 = layers.AveragePooling2D(pool_size=(2,2), strides=(2,2), padding="same")
pool2_flatten = layers.Flatten()

# 全连接层
fc1 = layers.Dense(units=120, activation='relu')
fc2 = layers.Dense(units=84, activation='relu')
fc3 = layers.Dense(units=10, activation='softmax')

# 2. 定义模型
model = keras.Sequential(layers=[x, con1, pool1, con2, pool2, pool2_flatten, fc1, fc2, fc3])

# 3. 定义训练参数
# sgd = SGD(learning_rate=0.01)

## 在tensorflow1.12中是lr
sgd = SGD(lr=0.01)

model.compile(
    optimizer=sgd,                      # 指定优化器
    loss='categorical_crossentropy',    # 指定损失函数
    metrics=['accuracy']
)

# 训练
model.fit(x_train, y_train, epochs=2)

# 最终结果
pred = model.predict(x_test)
accuracy = np.mean(np.argmax(pred, axis=1) == np.argmax(y_test, axis=1))
loss = model.evaluate(x_test, y_test)

print(accuracy, loss)