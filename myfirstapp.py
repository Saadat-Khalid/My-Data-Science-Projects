import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **Opening Price**, **Closing Price** and **Volume** of Apple!

##### By: Saadat Khalid Awan
""")

#define the ticker symbol

tickerSymbol = 'AAPL'

#get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker

tickerDF = tickerData.history(period='1d', start='2022-4-19', end='2023-4-19')

#Open High Low Close Volume Dividends Stock Splits

st.write("""
## Open Price
""")

st.line_chart(tickerDF.Open)

st.write("""
## Closing Price
""")

st.line_chart(tickerDF.Close)

st.write("""
## Volume Price
""")

st.line_chart(tickerDF.Volume)
