import tensorflow as tf

# 实现线性回归
# y = 0.7 * x + 0.8
# 矩阵运算
# tf.matmul(x, w)

# 平方
# tf.square(error)

# 均值
# tf.reduce_mean(error)

# 梯度下降优化
# tf.train.GradientDescentOptimizer(learning_rate)
# learning_rate: 学习率
# method
#   minimize(loss)

# 1. 准备数据
x_data = tf.random_normal([100, 1], mean=1.0, stddev=1.0, name="x_data")
y_true = tf.matmul(x_data, [[0.7]]) + 0.8

# 2. 定义变量
w = tf.Variable(tf.random_normal(shape=(1, 1)))
b = tf.Variable(tf.random_normal(shape=(1, )))

# 矩阵相乘
y = tf.matmul(x_data, w) + b

# 计算最小误差
loss = tf.reduce_mean(tf.square(y_true - y))

# 训练模型
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# 初始化变量操作
init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    # print(sess.run(x_data))
    # print(sess.run(y_ture))
    # print(sess.run(b))
    # print(sess.run(train_op))
    # print(b.eval())

    for i in range(1000):
        sess.run(train_op)
        print('第%d次， w的值为%f, b的值为%f, 缺省值为%f' % (i, w.eval(), b.eval(), loss.eval()))
