#Le-Net5神经网络
#实训老师提供数据集

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#权重和偏置的初始化函数
def weight_variable(shape):
	initial = tf.truncated_normal(shape=shape, mean=0, stddev=0.1, dtype=tf.float32)
	return tf.Variable(initial_value=initial)

def bias_variable(shape):
	initial = tf.random.truncated_normal(shape=[shape[-1]], mean=0, stddev=0.1, dtype=tf.float32)
	return tf.Variable(initial_value=initial)

#定义输入
x = tf.placeholder(tf.float32, [None, 28, 28, 1])
y = tf.placeholder(tf.float32, [None, 10])

#定义计算
def layer(in_x, in_w, in_b, padding='VALID'):
    o = tf.nn.conv2d(input=in_x, filter=in_w, strides=[1, 1, 1, 1], padding=padding)
    o = tf.math.add(o, in_b)
    o = tf.nn.relu(o)
    o = tf.nn.avg_pool(value=o, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    return o


#卷积层1
w1 = weight_variable(shape=[5, 5, 1, 6])
b1 = bias_variable(shape=[5, 5, 1, 6])
o1 = tf.nn.conv2d(input=x, filter=w1, strides=[1, 1, 1, 1], padding='SAME')
o1 = tf.nn.bias_add(o1, b1)
o1 = tf.nn.relu(o1)
o1 = tf.nn.avg_pool(value=o1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


#卷积层2
w2 = weight_variable(shape=[5, 5, 6, 16])
b2 = bias_variable(shape=[5, 5, 6, 16])
o2 = tf.nn.conv2d(input=o1, filter=w2, strides=[1, 1, 1, 1], padding='VALID')
o2 = tf.nn.bias_add(o2, b2)
o2 = tf.nn.relu(o2)
o2 = tf.nn.avg_pool(value=o2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


#卷积层3
w3 = weight_variable(shape=[5, 5, 16, 120])
b3 = bias_variable(shape=[5, 5, 16, 120])
o3 = tf.nn.conv2d(input=o2, filter=w3, strides=[1, 1, 1, 1], padding='VALID')
o3 = tf.nn.bias_add(o3, b3)
o3 = tf.nn.relu(o3)

#格式化，进入全连接层
o3 = tf.reshape(o3, [-1, 120])
w4 = weight_variable(shape=[120, 84])
b4 = bias_variable(shape=[120, 84])
o4 = tf.nn.relu(tf.matmul(o3, w4) + b4)
o4 = tf.nn.dropout(o4, 0.75)

w5 = weight_variable(shape=[84, 10])
b5 = bias_variable(shape=[84, 10])
o5 = tf.nn.softmax(tf.matmul(o4, w5) + b5)

y_ = o5

#损失函数
loss = tf.losses.sigmoid_cross_entropy(y, y_)

#训练算法
optimizer = tf.train.AdamOptimizer(0.0001)
trainer = optimizer.minimize(loss)

#加载训练数据
result = np.loadtxt("data/训练图片标签数据.txt", np.int)
result = result[0:1000] #为了速度可以只取部分训练集
print("训练样本个数：(%d)" % len(result))
labels = np.zeros((len(result), 10), dtype=np.int)
for i in range(len(result)):
    lb = result[i]
    labels[i][lb] = 1
data = np.zeros((len(result), 28, 28, 1), np.float32)
for i in range(len(result)):
    img = np.array([plt.imread("data/训练图片/TrainImage_%05d.bmp" % (i+1))])
    data[i, :, :, 0] = img
print("训练数据加载完毕！")

#加载测试数据
test_result = np.loadtxt("data/测试图片标签数据.txt", np.int)
test_result = test_result[0:200] #为了速度可以只取部分测试集
print("测试样本个数：(%d)" % len(test_result))
test_labels = np.zeros((len(test_result), 10), dtype=np.int)
for i in range(len(test_result)):
    lb = test_result[i]
    test_labels[i][lb] = 1
test_data = np.zeros((len(test_result), 28, 28, 1), np.float32)
for i in range(len(test_result)):
    img = np.array([plt.imread("data/测试图片/TestImage_%05d.bmp" % (i+1))])
    test_data[i, :, :, 0] = img
print("测试数据加载完毕！")

correct = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct, 'float'))


# 初始化
session = tf.Session()
global_v = tf.global_variables()
op_init = tf.initializers.variables(global_v)
session.run(op_init)
saver = tf.train.Saver()
model_path = "model/mymodel.ckpt"

TIMES = 500
batch_size = 100
batch = len(data) // batch_size
correct_rates =[]
for t in range(TIMES):
    loss_result = 0.0
    for idx in range(batch):
        _, loss_result = session.run([trainer, loss],
                                     feed_dict={
                                         x: data[idx * batch_size:(idx+1) * batch_size],
                                         y: labels[idx * batch_size:(idx+1) * batch_size]})
    #评估训练效果
    if t % 5 == 0:
    	#在测试集上评估准确率
        correct_rate = session.run(accuracy, feed_dict={x: test_data, y: test_labels})
        print('正确率: %5.2f%%，损失度：%f' % (correct_rate * 100.0, loss_result))
        correct_rates.append(correct_rate)
save_path = saver.save(session, model_path) #保存训练好的模型
print('训练完毕')