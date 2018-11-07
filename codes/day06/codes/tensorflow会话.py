import tensorflow as tf


a = tf.constant(4)
b = tf.constant(6)
# 创建一个占位符  没有指定行数, 但指定了列数
d = tf.placeholder(dtype=tf.float32, shape=(None, 3))
f = tf.placeholder(tf.float32, shape=(3, None))
c = tf.add(a, b)

# 会话
# target 目标主机
# graph 指定什么图
# config 就是展现出是什么执行
# with tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
#                                         log_device_placement=True)) as sess:
#
#     print(sess.run(a))
#     print(sess.run(c))

# run(fetches, feed_dict)
# fetches 可以指定列表， 元组（但里面一定要是tensorflow类型）
# feed_dict 参数允许调用者覆盖图中张量的值, 但是可以改变形状, 且只是在当前run中有用
with tf.Session() as sess:
    print(sess.run([a, c]))
    print(sess.run(a, feed_dict=({a: 10})))
    print(sess.run(f, feed_dict=({f: [[1], [2], [3]]})))
    print(sess.run(d, feed_dict=({d: [[1, 2, 3]]})))
    print(sess.run(a, feed_dict=({d: [[4, 2, 3]]})))
    # print(sess.run(d))