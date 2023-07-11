# Stock trading app

import os

import pandas as pd

# Get stock list from stock_info.csv
stock_list = pd.read_csv('stock_info.csv')

# Get ticker strings from stock_list
tickerStrings = stock_list['Ticker'].tolist()

import yfinance as yf

for ticker in tickerStrings:
    # Get data on this ticker
    tickerData = yf.Ticker(ticker)

    # Get today's date
    today = pd.Timestamp.today()

    # Get the date 3 months ago
    three_months_ago = today - pd.DateOffset(months=3)


    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=three_months_ago, end=today)

    print(tickerDf)

    # if dataframe is empty, delete the row from stock_info.csv
    if tickerDf.empty:
        print('empty')
        stock_list = stock_list[stock_list.Ticker != ticker]
        stock_list.to_csv('stock_info.csv', index=False)





