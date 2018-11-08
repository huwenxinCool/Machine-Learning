import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 获取数据
mnist = input_data.read_data_sets("../data/MNIST_DATA/", one_hot=True)

# 占位符
with tf.variable_scope("mnist_data"):
    x = tf.placeholder(tf.float32, shape=(None, 784))
    y_true = tf.placeholder(tf.float32, shape=(None, 10))

with tf.variable_scope("fc_model"):
    w = tf.Variable(tf.random_normal([784, 10]))
    b = tf.Variable(tf.random_normal([10]))

    # 矩阵相乘
    y_predict = tf.matmul(x, w) + b

with tf.variable_scope("softmax"):
    # softmax回归以及计算交叉熵
    # labels为真实值 logits 为预测
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))

# 梯度下降优化
with tf.variable_scope("optimizer"):
    # 学习率
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# 得出每次的准确率
with tf.variable_scope("accuracy"):
    equal_list = tf.equal(tf.argmax(y_true, 1), tf.argmax(y_predict, 1))
    accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

init = tf.global_variables_initializer()

if __name__ == '__main__':
    with tf.Session() as sess:
        sess.run(init)

        for i in range(40000):
            mnist_x, mnist_y = mnist.test.next_batch(100)
            # print(sess.run(train_op, feed_dict={x: mnist_x, y_true: mnist_y}).eval())
            sess.run(train_op, feed_dict={x: mnist_x, y_true: mnist_y})
            print("训练第%d步， 准确率为%f， 损失率为%f" % (
                i,
                sess.run(accuracy, feed_dict={x: mnist.test.images, y_true: mnist.test.labels}),
                # sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y}),
                sess.run(loss, feed_dict={x: mnist_x, y_true: mnist_y})
            ))
