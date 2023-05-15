# pip install yfinance

from ctypes import pythonapi
from gettext import install
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
import numpy as np


CURRENCY = 'EUR'

def getData(crypto):
  # Define time window
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    last_year_date = (now - timedelta(days=365)).strftime("%Y-%m-%d")

    start = pd.to_datetime(last_year_date)
    end = pd.to_datetime(current_date)

    data = yf.download(tickers=f'{crypto}-{CURRENCY}', start = start, end = end , interval = '1d')

    return data

# Call function to retrieve data on Bitcoin 
btc_data = getData('BTC')
# eth_data = getData('ETH')

# Plot graph
fig = go.Figure(
        data = [
            go.Candlestick(
                x = btc_data.index,
                open = btc_data.Open,
                high = btc_data.High,
                low = btc_data.Low,
                close = btc_data.Close
            ) 
        ] )
fig.update_layout(
    title = f'Time Series with Range slider for BTC',
    xaxis_title = 'Date',
    yaxis_title = f'Price ({CURRENCY})',
    xaxis_rangeslider_visible = True
)
fig.update_yaxes(tickprefix=CURRENCY)

fig.show()