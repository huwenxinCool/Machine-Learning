import tensorflow as tf

# tensorflow变量的特点
# 1，存储持久化
# 2， 可修改值
# 3， 可指定训练

# tf.Variable(initial_value, trainable,collections, name)
# initial_value: 初始化的值
# trainable: 是否被训练
# collection: 新变量将添加到列出的图集合中的collections

# 使用变量的值，首先要开启初始化
# init = tf.global_variables_initalizer()   初始化对象
# sess.run(init)    进行初始化

a = tf.Variable(tf.random_normal(shape=(2, 2)))
b = tf.Variable(1)

# 共享变量的定义

# 1. 命名相同
# c = tf.Variable(777, name='var')
# d = tf.Variable(888, name='var')

# 修改命名空间
# 只是在名字前面加了个name的路径一样的东西
# with tf.variable_scope("name"):
#     c = tf.Variable(777, name='var')
#     d = tf.Variable(888, name='var')

# 这才是共享变量，而且只有第一个值有效
with tf.variable_scope("name", reuse=tf.AUTO_REUSE):
    c = tf.get_variable(initializer=777, name="var", dtype=tf.int32)
    d = tf.get_variable(initializer=888, name="var", dtype=tf.int32)

print(c)
print(d)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a))
    print(sess.run(b))
    print(sess.run(c))
    print(sess.run(d))