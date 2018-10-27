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