import tensorflow as tf

a = tf.constant([1, 2, 3, 4])
b = tf.placeholder(tf.float32, shape=(None, 3))

# 设置形状， 确定了就不能该变了
b.set_shape([1, 3])

c = tf.reshape(a, [2, 2])


with tf.Session() as sess:
    print(sess.run(a))
    print(b.shape)
    print(sess.run(b, feed_dict=({b: [[1, 2, 3]]})))
    print(sess.run(c))