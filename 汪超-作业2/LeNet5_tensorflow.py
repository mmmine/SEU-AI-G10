import tensorflow as tf
import numpy as np
import tensorflow.keras
import tensorflow.keras.datasets.mnist as mnist_keras
from tensorflow.examples.tutorials.mnist import input_data


# 导入数据集
mnist = input_data.read_data_sets("../datasets/MNIST_qata", one_hot=True)

# 单通道的图片
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
trX = trX.reshape(-1, 28, 28, 1)
teX = teX.reshape(-1, 28, 28, 1)


# 初始化权重的函数
def get_weights(shape):
    w = tf.Variable(tf.random_normal(shape = shape, mean=0, stddev=0.1, dtype=tf.float32))
    b = tf.Variable(tf.random_normal(shape=[shape[-1]], mean=0, stddev=0.1, dtype=tf.float32))
    return w, b
    
def get_model(x, w1, b1, w2, b2, w3, b3, w4, b4, w5, b5, p_keep_conv):
    ## 第一个可训练层， 卷积层
    l1 = tf.nn.conv2d(input=x, filter=w1, strides=[1,1,1,1], padding="SAME")
    l1 = tf.nn.bias_add(l1, b1)
    l1 = tf.nn.relu(l1)
    l1_pool = tf.nn.avg_pool(value=l1, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
    # dropout防止过拟合
    l1_pool = tf.nn.dropout(l1_pool, p_keep_conv)
    
    ## 第二个可训练层，卷积层
    l2 = tf.nn.conv2d(input=l1_pool, filter=w2, strides=[1,1,1,1], padding="VALID")
    l2 = tf.nn.bias_add(l2, b2)
    l2 = tf.nn.relu(l2)
    l2_pool = tf.nn.avg_pool(value=l2, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
    l2_pool = tf.nn.dropout(l2_pool, p_keep_conv)
    
    # 下面有三层全连接层
    fc1 = tf.reshape(l2_pool, [-1, w3.get_shape().as_list()[0]])    # 5 * 5 * 1 * 16
    
    fc1 = tf.matmul(fc1, w3) + b3
    fc1 = tf.nn.relu(fc1)
    fc1 = tf.nn.dropout(fc1, p_keep_conv)
    
    fc2 = tf.matmul(fc1, w4) + b4
    fc2 = tf.nn.relu(fc2)
    fc2 = tf.nn.dropout(fc2, p_keep_conv)
    
    fc3 = tf.matmul(fc2, w5) + b5
    
    return fc3

# 卷积层
w1, b1 = get_weights([5, 5, 1, 6])
w2, b2 = get_weights([5, 5, 6, 16])

# 全连接层
w3, b3 = get_weights([400, 120])
w4, b4 = get_weights([120, 84])
w5, b5 = get_weights([84, 10])

# 参数
x = tf.placeholder(tf.float32, [None, 28, 28, 1])
y = tf.placeholder(tf.float32, [None,10])
p_keep_conv = tf.placeholder(tf.float32)
epoch = 100

pred = get_model(x, w1, b1, w2, b2, w3, b3, w4, b4, w5, b5, p_keep_conv)

## 定义损失函数， 并指定优化方法
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
train = tf.train.AdamOptimizer(0.0001).minimize(loss)

correct = tf.equal(tf.argmax(teY, axis=1), tf.argmax(pred, axis=1))
accuracy = tf.reduce_mean(tf.cast(correct, 'float'))


# 训练
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    
    for i in range(epoch):
        training_batch = zip(range(0, len(trX), 128), range(128, len(trX)+1, 128))
        for start, end in training_batch:
            t, l = sess.run([train, loss], feed_dict={x:trX[start:end], y:trY[start:end], p_keep_conv:0.7})
        
        print("%d, loss:" % i, l)
    # 准确度
    acc = sess.run(accuracy, feed_dict={x:teX, y:teY, p_keep_conv:1})
    print("准确度：", acc)