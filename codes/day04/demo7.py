# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。

# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
import talib
def init(context):
    # 在context中保存全局变量
    context.stocks = index_components("000300.XSHG")
    # 短线
    context.SHORTPERIOD = 12
    # 长线
    context.LONGPERIOD = 26
    # 周期
    context.SMOOTHPERIOD = 9
    context.OBSERVATION = 100
    # 实时打印日志

# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    pass


# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
   # 利用MACD来实现
   for stock_code in context.stocks:
       prices = history_bars(stock_code, context.OBSERVATION, '1d', 'close')
       
       # macd 为差离值， macdsignal 为信号线， macdhist为柱状图
       macd, macdsignal, macdhist = talib.MACD(prices, context.SHORTPERIOD, context.LONGPERIOD, context.SMOOTHPERIOD)
       
       if macd[-2] < macdsignal[-2] and macd[-1] > macdsignal[-1]:
           order_percent(stock_code, 0.2)
    
       if macd[-2] > macdsignal[-2] and macd[-1] < macdsignal[-1]:
           curPosition = context.portfolio.positions[stock_code].quantity
           if curPosition > 0:
               order_target_value(stock_code, 0)
    

# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    pass