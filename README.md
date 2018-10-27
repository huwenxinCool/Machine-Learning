# Machine-Learning
- 什么是机器学习？
- 从数据中自动获取模型，并对模型进行预测

- 数据集的构成
    - 结构：　目标值　＋ 特征值
    - 没一列就是特征, 没一行的数据可以叫做样本

- 机器学习的算法:
    - 监督学习
        - 给的数据有特征值, 目标值和标准答案就是监督学习
        - 监督学习又分为两类:
            - 分类: 具有明显的分类, 比如动物是什么类型的, 明天是阴天,还是雨天
            - 回归: 连续型数据, 比如房价走势, 温度预测等
        - 无监督学习:
            - 有目标值和特征值,但没有标准答案

- 机器学习开发流程:
    - 1.拿到原始数据
    - 2.数据特征工程提取
    - 3.进行算法学习, 获取模型
    - 4.模型评估(数据测试)
        - 如果模型不合格就再次进入到第三步
    - 5.模型应用

## 特征工程
- 数据集
    - 数据集分为训练集和测试集
    - Kaggle网址：https://www.kaggle.com/datasets
    - UCI数据集网址： http://archive.ics.uci.edu/ml/
    - scikit-learn网址：http://scikit-learn.org/stable/datasets/index.html#datasets

### Scikit-learn
- Scikit-learn 是python用来学习机器学习的一个库, 里面有许多知名算法的实现, 文档完善, 丰富的API, 
- 使用版本为0.19.1
- 安装: pip install Scikit-learn==0.19.1
    - 需要numpy, pandas,Scipy这些库
    - 具体例子在codes里面

- 数据集的划分
- sklearn.model_selection.train_test_split(arrays, *options)
    - x 数据集的特征值
    - y 数据集的标签值
    - test_size 测试值的大小
    - random_state 随机数的种子
    - return 训练标签, 测试标签(默认随机取样)
### 特征工程
- 为什么需要特征工程?
    - 数据和特征决定了机器学习的上限,而逻辑和算法只是逼进这个值
- 什么是特征工程?
    - 特征工程就是利用专业的背景知识和技巧处理数据,使特征在机器学习算法上发挥更好的作用
- 特征工程包含
    - 特征提取
    - 特征预处理
    - 特征降维

# 特征提取
- 什么是特征提取?
    - 将任意数据(文本, 图像等)转换为可用于机器学习的数字特征
    - *特征值是为了让计算机更好的去理解特征值
- 几种常见的特征提取
    - 字典特征提取(特征离散化)
    - 文本特征提取
    - 图像特征提取(深度学习介绍)
- 特征提取的API
    - sklearn.feature_extraction
        - DictVectorizer(sparse=True)
        - 对字典类型进行特征提取
        - sparse默认为True, False变成了one-hot编码格式
    - sklearn.feature_extraction.text
        - CountVectorizer
            - 对文本数据进行特征提取.但是对中文不友好(处理中文之前要使用jieba进行分词)
        - TfidfVectorizer
            - 是进行一个词在多篇文章中出现的概率(是分类算法之前的数据处理常用到的)
# 特征预处理
- 什么是特征预处理
    - 通过一些转换函数将特征数据转换成更加合适算法的模型的特征数据过程
    - 就是把特征值转换成同一级别的数据

- 主要有两种方法:
    - 归一化
    - 标准化
- 为什么要进行归一化/标准化?
    - 特征的单位或者大小相差较大，或者某特征的方差相比其他的特征要大出几个数量级，容易影响（支配）目标结果，使得一些算法无法学习到其它的特征
## 归一化
- 公式
    - x’ = (x - min)/(max - min)
    - x’’ = x’ * (mx - mi) + mi
    - 作用于每一列，max为一列的最大值，min为一列的最小值,那么X’’为最终结果，mx，mi分别为指定区间值默认mx为1,mi为0
- API
    - sklearn.perprocession.MinMaxScaler(feature_range=(0, 1))
    - MinMaxScaler.fit_transform(x)
        - x:numpy array格式的数组
- 归一化总结
    - 注意最大值最小值是变化的，另外，最大值与最小值非常容易受异常点影响，所以这种方法鲁棒性较差，只适合传统精确小数据场景。
## 标准化
- 通过对原始数据进行变换把数据变换到均值为0,标准差为1范围内
- 公式:
    - x’ = (x - mean)/σ
    - 作用于每一列，mean为平均值，σ为标准差
    - 对于归一化来说：如果出现异常点，影响了最大值和最小值，那么结果显然会发生改变
    - 对于标准化来说：如果出现异常点，由于具有一定数据量，少量的异常点对于平均值的影响并不大，从而方差改变较小。
- API
    - sklearn.preprocessing.StandardScaler
        - 处理之后每列来说所有数据都聚集在均值0附近标准差差为1
        - StandardScaler.fit_transform(X)
            - X:numpy array格式的数据[n_samples,n_features]
- 标准化总结
    - 在已有样本足够多的情况下比较稳定，适合现代嘈杂大数据场景。
#特征降维
- 什么是降维
    - 降维是指在某些限定条件下，降低随机变量(特征)个数，得到一组“不相关”主变量的过程

- 降维的两种方式
    - 特征选择
    - 主成分分析（可以理解一种特征提取的方式）
- 什么是特征选择
    - 数据中包含冗余或无关变量（或称特征、属性、指标等），旨在从原有特征中找出主要特征。
    - 方法:
        - Filter(过滤式)：主要探究特征本身特点、特征与特征和目标值之间关联
            - 方差选择法：低方差特征过滤
            - 相关系数
        - Embedded (嵌入式)：算法自动选择特征（特征与目标值之间的关联）
            - 决策树:信息熵、信息增益
            - 正则化：L1、L2
            - 深度学习：卷积等
    -  模块
        - sklearn.feature_selection
##  过滤式
### 低方差特征过滤
    - 删除低方差的一些特征，前面讲过方差的意义。再结合方差的大小来考虑这个方式的角度。

        - 特征方差小：某个特征大多样本的值比较相近
        - 特征方差大：某个特征很多样本的值都有差别
- API
    - sklearn.feature_selection.VarianceThreshold(tgreshold=0.0)
        - 删除所有低方差特征
        - Variance.fit_transform(X)
        - X:numpy array格式的数据[n_samples,n_features]
        - 返回值：训练集差异低于threshold的特征将被删除。默认值是保留所有非零方差特征，即删除所有样本中具有相同值的特征。
### 相关系数
    - 皮尔逊相关系数(Pearson Correlation Coefficient)
    - 反映变量之间相关关系密切程度的统计指标

    - 特点

        - 相关系数的值介于–1与+1之间，即–1≤ r ≤+1。其性质如下：

        - 当r>0时，表示两变量正相关，r<0时，两变量为负相关
        - 当|r|=1时，表示两变量为完全相关，当r=0时，表示两变量间无相关关系
当0<|r|<1时，表示两变量存在一定程度的相关。且|r|越接近1，两变量间线性关系越密切；|r|越接近于0，表示两变量的线性相关越弱
        - 一般可按三级划分：|r|<0.4为低度相关；0.4≤|r|<0.7为显著性相关；0.7≤|r|<1为高度线性相关
        - 这个符号：|r|为r的绝对值， |-5| = 5
    - API
        - scipy.stats.pearsonr
            - x : (N,) array_like
            - y : (N,) array_like Returns: (Pearson’s correlation coefficient, p-value)
# 主成分分析
- 什么是主成分分析(PCA)
    - 定义：高维数据转化为低维数据的过程，在此过程中可能会舍弃原有数据、创造新的变量
    - 作用：是数据维数压缩，尽可能降低原数据的维数（复杂度），损失少量信息。
    - 应用：回归分析或者聚类分析当中
- API
    - sklearn.decomosition.PCA(n_components=None)
        - 将数据分解成较底维数空间
        - n_components:
            - 小数:表示保留百分之多少的信息
            - 整数:减少到多少特征
        - PCA.fit_transform(X) X:numpy array格式的数据[n_samples,n_features]
        - 返回值：转换后指定维度的array