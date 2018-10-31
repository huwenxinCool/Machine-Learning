# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。

# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    # 在context中保存全局变量
    # logger.info(industry('农业'))
    # logger.info(industry("A01"))
    # logger.info(sector('信息技术'))
    # logger.info(index_components('000001.XSHG'))
    context.s1 = '000001.XSHE'
    # logger.info(history_bars(context.s1, 5, '1d', "close"))
    # history_bars(order_book_id, bar_count, frequency, skip_suspended=True, include_now=False) 获取历史合约数据
    # history_bars 不能在init中使用
    scheduler.run_monthly(data, 1)
    

def data(context, bar_dict):
    logger.info('111111111111111')
    # scheduler.run_daily(data1, 1)
    

def data1(context, bar_dict):
    logger.info('222222222222')

# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    # logger.info(history_bars(context.s1, 5, '1d', 'close'))
    # q = query(fundamentals.eod_derivative_indicator.pe_ratio, fundamentals.income_statement.revenue).filter(fundamentals.eod_derivative_indicator.pe_ratio > 25).filter(fundamentals.income_statement.revenue > 5.47843e+08).order_by(fundamentals.eod_derivative_indicator.pe_ratio.desc()).limit(3)
    # fund = get_fundamentals(q).T
    # logger.info(fund)
    
    pass

# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    # 开始编写你的主要的算法逻辑

    # bar_dict[order_book_id] 可以拿到某个证券的bar信息
    # context.portfolio 可以拿到现在的投资组合信息

    # 使用order_shares(id_or_ins, amount)方法进行落单

    # TODO: 开始编写你的算法吧！
    pass

# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    pass