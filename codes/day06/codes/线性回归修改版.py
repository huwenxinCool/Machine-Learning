import tensorflow as tf

# 1. 准备数据
with tf.variable_scope("data"):
    x_data = tf.random_normal([100, 1], mean=1.0, stddev=1.0, name="x_data")
    y_true = tf.matmul(x_data, [[0.7]]) + 0.8

# 2. 定义变量
with tf.variable_scope("var"):
    w = tf.Variable(tf.random_normal(shape=(1, 1)))
    b = tf.Variable(tf.random_normal(shape=(1, )))

# 矩阵相乘
    y = tf.matmul(x_data, w) + b

# 计算最小误差
with tf.variable_scope('loss'):
    loss = tf.reduce_mean(tf.square(y_true - y))

# 增加变量显示
tf.summary.scalar(name='loss', tensor=loss)
tf.summary.histogram(name='w', values=w)
tf.summary.histogram(name='b', values=b)

# 合并
merge = tf.summary.merge_all()

# 训练模型
with tf.variable_scope('train_op'):
    train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# 初始化变量操作
init = tf.global_variables_initializer()

# 保存模型
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    file_write = tf.summary.FileWriter('./demo/', graph=sess.graph)
    # for i in range(1000):
    #     sess.run(train_op)
    #     print('第%d次， w的值为%f, b的值为%f, 缺省值为%f' % (i, w.eval(), b.eval(), loss.eval()))
    #     summary = sess.run(merge)
    #     file_write.add_summary(summary, i)
    # # 保存模型
    # saver.save(sess, "./model/liner.ckpt")

    # 模型加载
    saver.restore(sess, "./model/liner.ckpt")
    print( w.eval(), b.eval(), loss.eval())