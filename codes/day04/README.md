# 量化交易
- 定义：量化交易(量化投资)是指借助现代统计学和数学(机器学习)的方法，利用计算机技术来进行交易的证券投资方式。
- 目的：获得可以持续的、稳定且高于平均收益的超额回报。
## 量化交易的分类
- 趋势性交易
	- 适合一些主观交易的高手，用技术指标作为辅助工具在市场中如鱼得水的，但如果只用各种技术指标或指标组合作为核心算法构建模型，从未见过能长期盈利的。
	- 一般也会做一些量化分析操作，使用编程如python/matlab 。
- 市场中性
	- 在任何市场环境下风险更低，收益稳定性更高，资金容量更大。适合一些量化交易者，发现市场中的alpha因子赚取额外收益，例如股票与股指期货的对冲策略等。
	- 会做一些量化分析操作，使用编程如python/matlab。
- 高频交易
	- 在极短的时间内频繁买进卖出，完成多次大量的交易，此类交易方式对硬件系统以及市场环境的要求极高，所以只有在成熟市场中的专业机构才会得到应用
	- 适合一些算法高手，使用C/C++编程语言，去进行算法交易，对软硬件条件要求比较高。
## 量化交易的优势
- 严格的纪律性
- 完备的系统性
	- 完备的系统性具体表现为“三多”。
		- 首先表现在多层次，包括在大类资产配置、行业选择、精选个股三个层次上都有模型；
		- 其次是多角度，量化交易的核心投资思想包括宏观周期、市场结构、估值、成长、盈利质量、分析师盈利预测、市场情绪等多个角度；
		- 再者就是多数据，就是海量数据的处理。人脑处理信息的能力是有限的，当一个资本市场只有100只股票，这对定性投资基金经理是有优势的，他可以深刻分析这100家公司。但在一个很大的资本市场，比如有成千上万只股票的时候，强大的定量化交易的信息处理能力能反映它的优势，能捕捉更多的投资机会，拓展更大的投资机会。
	- 靠数学模型取胜
		- 股票实际操作过程中，运用概率分析，提高买卖成功的概率
## 量化交易的研究流程
- 量化回测框架提供完整的数据，以及回测机制进行策略评估研究，并能够实时进行模拟交易。为实盘交易提供选择。
	- 流程包含的内容
		- 获取数据
			- 公司财务、新闻数据
			- 基本行情数据
		- 数据分析挖掘
			- 传统分析方法、机器学习，数据挖掘方法
			- 数据处理，标准化，去极值，中性化分组回测，行业分布
		- 构建策略
			- 获取历史行情，历史持仓信息，调仓记录等
			- 止盈止损单，限价单，市价单
		- 回测
			- 股票涨跌停、停复牌处理
			- 市场冲击，交易滑点，手续费
		- 策略分析
			- 收益指标, 风险指标
			- 订单分析，成交分析，持仓分析
		- 模拟交易
			- 接入实时行情，实时获取成交回报
			- 实时监控，实时归因分析
		- 实盘交易
			- 接入真实券商账户
		- 演示结果
### 什么是策略
- 量化策略是指使用计算机作为工具，通过一套固定的逻辑来分析、判断和决策。 量化策略既可以自动执行，也可以人工执行。其实策略也可以理解为，分析数据之后，决策买什么以及交易时间。
### 什么是回测
- 通过以前的行情数据进行测试，调整系统，借此提高交易系统的可靠性。回测环境是一个所有风险已知的环境。回测应该运行时间长达2-3年，最好是一轮牛熊，详细的有效的交易次数应当不低于100次，避免偶然性。
## 回测框架介绍
- Zipline
	- Zipline本身只支持美国的证券，无法更好的使用数据，本地运行速度慢
- 云端的框架
	- 米框
		- https://www.ricequant.com/
	- 聚宽
### 米框
- 策略创建运行流程
	- 里面主要是四个方法
		- def init(context)
			- 运行时就会执行一次
		- def before_trading(context)
			- 每次开盘前就会执行
		- def handle_bar(context, bar_dict)
			- 会看频率执行，主要看自己配置（可以每天，也可以每分钟）
		- def after_trading(context)
			- 每天收盘会执行
#### 数据获取接口
- 获取行业、板块以及指数成分股票列表
	- industry(code) 行业的股票列表
		- code 为行业名称或者代码也行
		- API https://www.ricequant.com/api/research/chn#research-API-current_performance
			- industry("A01")     industry('农业')
		- 返回的是这一行的所有股票
	- sector(code)  板块的股票列表
		- sector('信息技术')
	- index_components 指数成分股
		- index_components(order_book_id, date=none)
		- 获取某一指数的股票构成列表，也支持指数的历史构成查询

			- index_components('000001.XSHG')
		- 自定义股票池
			- context.hs300 = index_components('000300.XSHG')
#### 获取股票合约数据
- history_bars - 某一合约历史数据
	- history_bars(order_book_id, bar_count, frequency, fields=None, skip_suspended=True, include_now=False)
	- 获取指定合约的历史行情，同时支持日以及分钟历史数据。不能在init中调用。
		- order_book_id	str	合约代码，必填项
		- bar_count	int	获取的历史数据数量，必填项
		- frequency	str	获取数据什么样的频率进行。'1d'或'1m'分别表示每日和每分钟，必填项。您可以指定不同的分钟频率，例如'5m'代表5分钟线
		- fields	strOR str list	返回数据字段。必填项。见下方列表
		- skip_suspended	bool	是否跳过停牌，默认True，跳过停牌
		- include_now	bool	是否包括不完整的bar数据。默认为False，不包括。举例来说，在09:39的时候获取上一个5分钟线，默认将获取到09:31~09:35合成的5分钟线。如果设置为True，则将获取到09:36~09:39之间合成的"不完整"5分钟线
####  获取财务数据
- get_fundamentals  查询财务数据
	- get_fundamentals(query, entry_date=None, interval='1d', report_quarter=False)
		- query	SQLAlchemyQueryObject	SQLAlchmey的Query对象。其中可在'query'内填写需要查询的指标，'filter'内填写数据过滤条件。具体可参考 sqlalchemy's query documentation 学习使用更多的方便的查询语句。从数据科学家的观点来看，sqlalchemy的使用比sql更加简单和强大
		- entry_date	str, datetime.date, datetime.datetime, pandasTimestamp	查询财务数据的基准日期，应早于策略当前日期。默认为策略当前日期前一天。
		- interval	str	查询财务数据的间隔，默认为'1d'。例如，填写'5y'，则代表从entry_date开始（包括entry_date）回溯5年，返回数据时间以年为间隔。'd' - 天，'m' - 月， 'q' - 季，'y' - 年
		- report_quarter	bool	是否显示报告期，默认为False，不显示。'Q1' - 一季报，'Q2' - 半年报，'Q3' - 三季报，'Q4' - 年报
	- query() 通过fundamentals获取以上的属性 https://www.ricequant.com/fundamentals#stk_fundamental_gen
	- 列如：  q = query(fundamentals.eod_derivative_indicator.pe_ratio, fundamentals.income_statement.revenue).filter(fundamentals.eod_derivative_indicator.pe_ratio > 25).filter(fundamentals.income_statement.revenue > 5.47843e+08).order_by(fundamentals.eod_derivative_indicator.pe_ratio.desc()).limit(3)
    - fund = get_fundamentals(q).T
    - logger.info(fund)
    - 过滤指标条件
		- query().filter：过滤大小
		- query().order_by：排序
		- query().limit()：限制数量
		- fundamentals.stockcode.in_()：在指定的股票池当中过滤
- scheduler定时器定时数据获取
	- scheduler.run_daily - 每天运行
	- scheduler.run_weekly - 每周运行
	- scheduler.run_monthly - 每月运行
	- 只能在init中调用

	- 使用
		- scheduler.run_monthly(function, tradingday=t)
		- 需要传入的函数名
		- tradingday 范围为[-23,1], [1,23] ，例如，1代表每月第一个交易日，-1代表每月倒数第一个交易日，用户必须指定

## 回测交易接口
- 用于股票的交易函数
	- order_shares(id_or_ins, amount, style=MarketOrder()) - 指定股数交易（股票专用）
		- id_or_ins	str或instrument对象	order_book_id或symbol或instrument对象，用户必须指定
		- amount	float-required	需要落单的股数。正数代表买入，负数代表卖出。将会根据一手xx股来向下调整到一手的倍数，比如中国A股就是调整成100股的倍数。
		- style	OrderType	订单类型，默认是市价单。目前支持的订单类型有：style=MarketOrder() and style=LimitOrder(limit_price)
	- order_percent(id_or_ins, percent, style=OrderType) - 一定比例下单（股票专用）
		- id_or_ins	str或instrument对象	order_book_id或symbol或instrument object，用户必须指定
		- percent	float	占有现有的投资组合价值的百分比。正数表示买入，负数表示卖出。用户必须指定
		- style	OrderType	订单类型，默认是市价单。目前支持的订单类型有：style=MarketOrder()style=LimitOrder(limit_price)
	- order_value - 指定价值交易（股票专用）
	- order_lots  - 指定手数交易（股票专用）
	- order_target_percent(id_or_ins, percent, style=OrderType) - 目标比例下单（股票专用）
		- id_or_ins	str或instrument对象	order_book_id或symbol或instrument object，用户必须指定
		- percent	float	仓位最终所占投资组合总价值的目标百分比。
		- style	OrderType	订单类型，默认是市价单。目前支持的订单类型有：style=MarketOrder()style=LimitOrder(limit_price)
	- 更多详细内容参考：https://www.ricequant.com/api/python/chn#methods-implement-after-trading

## 投资组合
- 定义： 投资组合是由投资人或金融机构所持有的股票、债券、金融衍生产品等组成的集合，目的是分散风险。

- context属性
	- context.now 查看当前时间
	- context.portfolio - 投资组合信息
	- context.stock_account - 股票资金账户信息
- portfolio对象
	- cash	float	可用资金，为子账户可用资金的加总
	- frozen_cash	float	冻结资金，为子账户冻结资金加总
	- total_returns	float	投资组合至今的累积收益率
	- daily_returns	float	投资组合每日收益率
	- daily_pnl	float	当日盈亏，子账户当日盈亏的加总
	- market_value	float	投资组合当前的市场价值，为子账户市场价值的加总
	- total_value	float	总权益，为子账户总权益加总
	- units	float	份额。在没有出入金的情况下，策略的初始资金
	- unit_net_value	float	单位净值
	- static_unit_net_value	float	静态单位权益
	- transaction_cost	float	当日费用
	- pnl	float	当前投资组合的累计盈亏
	- start_date	datetime.datetime	策略投资组合的回测/实时模拟交易的开始日期
	- annualized_returns	float	投资组合的年化收益率
	- positions	dict	一个包含所有仓位的字典，以order_book_id作为键，position对象作为值，关于position的更多的信息可以在下面的部分找到。
- Position对象
	- order_book_id	str	合约代码
	- quantity	int	当前持仓股数
	- pnl	float	持仓累计盈亏
	- sellable	int	该仓位可卖出股数。T＋1的市场中sellable = 所有持仓-今日买入的仓位
	- market_value	float	获得该持仓的实时市场价值
	- value_percent	float	获得该持仓的实时市场价值在总投资组合价值中所占比例，取值范围[0, 1]
	- avg_price	float	平均建仓成本
## 策略评价指标
- 收益指标
	- 回测收益率
		- 策略在期限内的收益率。
	- 复利
		- 复利是指一笔资金除本金产生利息外，在下一个计息周期内，以前各计息周期内产生的利息也计算利息的计息方法。
	- 年化收益率
		- 采用了复利累积以及Actual/365 Fixed的年化方式计算得到的年化收益。
		- 我们更加注重年化收益率，对于股票来讲，年化达到15~30%已经算是比较好的策略。年化收益率越高越好
	- 基准收益率
		- 相同条件下，一个简单的买入并持有基准合约策略的收益率（默认基准合约为沪深300指数，这里假设指数可交易，最小交易单位为1）。
		- 基准收益率拿来对比我们的策略收益率，策略的表现期望超过基准收益率才获得了比较好的收益
- 风险指标
- 风险指标指的是在获得收益的时候，承担一些风险值
	- 最大回撤
		- 最大回撤率：在选定周期内任一历史时点往后推，产品净值走到最低点时的收益率回撤幅度的最大值。最大回撤用来描述描述任一投资者可能面临的的最大亏损。最大回撤是一个重要的风险指标，对于对冲基金和数量化策略交易，该指标比波动率还重要。
		- 公式可以这样表达：D为某一天的净值，i为某一天，j为i后的某一天，Di为第i天的总权益，Dj则是Di后面某一天的总权益。drawdown=max（Di-Dj）/Di，其实就是对每一个净值进行回撤率求值，然后找出最大的。可以使用程序实现。
		- 最大回撤越小越好，最大回撤最好保持10~30%之间
	- 夏普比率
		- 若夏普比率为2.4，代表投资者风险每增长1%，换来的是2.4%的多余收益。夏普比率越大，说明单位风险所获得的风险回报越高。
		- 注：夏普比率越高越好，达到1.5已经是很好的结果，在1.0左右都可以
## 实现第一个股票策略
