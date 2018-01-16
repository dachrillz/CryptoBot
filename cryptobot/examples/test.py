from datetime import datetime
import backtrader as bt


class SmaCross(bt.SignalStrategy):
    params = (('pfast', 10), ('pslow', 30),)

    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))


cerebro = bt.Cerebro()

data = bt.feeds.YahooFinanceData(dataname='YAHOO', fromdate=datetime(2011, 1, 1),
                                 todate=datetime(2012, 12, 31))
cerebro.adddata(data)

cerebro.addstrategy(SmaCross)
cerebro.run()
cerebro.plot()