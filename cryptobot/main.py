
import backtrader as bt
import datetime
import os.path
import sys

if __name__ == '__main__':

    name_of_data = 'example_data.txt' #File name for data file from data folder.
    strategy_name = 'testStrategy2' #File name for strategy in strategy folder.
    strategy_path = 'strategies.' + strategy_name

    #Get the correct strategy based on string input @TODO: Document that the name of the class has to be same as the file name.
    module = __import__(strategy_path)
    my_class = getattr(module, strategy_name)
    strategy_instance = my_class.Strategy


    #Create cerebro (The back trader engine)
    cerebro = bt.Cerebro()


    #Get Data in folder
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    modpath = os.path.dirname(modpath)
    modpath += '/data/' + name_of_data

    #add Strategy
    cerebro.addstrategy(strategy_instance)


    # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=modpath,
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2000, 12, 31),
        reverse=False)

    #Add the data to cerebro
    cerebro.adddata(data)

    #Set initial cash
    cerebro.broker.setcash(10000.0)

    print("Running main.py with %.2f" % cerebro.broker.getvalue())

    cerebro.run() #run the engine

    print(print("Ran the model and now has: %.2f" % cerebro.broker.getvalue()))



