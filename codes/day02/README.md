# 分类算法
- sklearn的转换器和估计器
	- 什么是转换器
		- 就是特征工程的接口称为转换器， 其中转换器分为这么几种
		- fit_transform
		- fit
		- transform	

	- 什么是估计器
	- 估计器（estimator)分为几种
	- 用于分类的估计器
		- sklearn.neighbors K近邻算法
		- sklearn.naive_bayes 贝叶斯
		- sklearn.linear_model.LogisticRegression 逻辑回归
		- sklearn.tree 决策树与随机森林
	- 用于回归的估计器
		- sklearn.linear_model.LinearRegression 线性回归
		- sklearn.linear_model.Ridge 岭回归
	- 用于无监督学习的估计器
		- sklearn.cluster.KMeans 聚类

### K-近邻算法（KNN)原理
- 定义
	- 如果一个样本在特征空间中的k个最相似(即特征空间中最邻近)的样本中的大多数属于某一个类别，则该样本也属于这个类别。
- 列如：
	- a(a1, a2, a3), b(b1, b2, b3)
	- 公式：（（a1 - b1）*（a1 - b1）+ （a2 - b2）*（a2 - b2） + （a3 - b3）*（a3 - b3）） ** 0.5
	- 就是距离公式
- API 
	- sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, algorithm="auto")
	- n_neighbors：int,可选（默认= 5），k_neighbors查询默认使用的邻居数
	- algorithm：{‘auto’，‘ball_tree’，‘kd_tree’，‘brute’}，可选用于计算最近邻居的算法：‘ball_tree’将会使用 BallTree，‘kd_tree’将使用 KDTree。‘auto’将尝试根据传递给fit方法的值来决定最合适的算法。 (不同实现方式影响效率)
- 案列1： 鸢尾花种类预测
- 案例2：预测签到位置
	- 发现正确率只有0.4 明显就不可以  需要另外一种解决办法