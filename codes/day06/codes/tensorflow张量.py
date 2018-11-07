import tensorflow as tf

# 什么是张量？
# 张量就是一个n维数组。类型为tf.Tensor. 具有两个特别重要的属性
# dtype: 数据类型
# shape: 形状


# 创建张量的几种方法：
a = tf.zeros(shape=(3, 4))
b = tf.ones(shape=(3, 3))
c = tf.zeros_like(b, dtype=tf.int32, name="ccc")
d = tf.ones_like(a, name='ccc')
f = tf.fill([2, 2], 7, name='ccc')
# fill 指定值来创建
# fill(dims, value, name)
# dims 是形状
# value 是值
# name 是空间命名

# constant 也是可以指定形状
e = tf.constant(6, shape=(3, 3), name='ccc')

print(type(a))
print(a)
print(c)
print(d)
print(f)
print(e)

with tf.Session() as sess:
    print(sess.run(a))
    print(sess.run(b))
    print(sess.run(c))
    print(sess.run(d))
    print(sess.run(f))
    print(sess.run(e))