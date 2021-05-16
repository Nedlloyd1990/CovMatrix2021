import yfinance as yf
import streamlit as st
import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

Tickername=[]
Interval=[]
Pre_stochrsi_list=[]
Curr_stochrsi_list=[]


st.title("Correlation and dependence")
st.write("In statistics, correlation or dependence is any statistical relationship, whether causal or not, between two random variables or bivariate data. In the broadest sense correlation is any statistical association, though it commonly refers to the degree to which a pair of variables are linearly related.")

st.write("A correlation coefficient of 1 indicates a perfect positive correlation between the prices of two stocks, meaning the stocks always move the same direction by the same amount. ... If two stocks have a correlation coefficient of 0, it means there is no correlation and, therefore, no relationship between the stocks")

st.write("Data source used is Yahoo Finance")


d3 = st.sidebar.date_input("Select Date",dt.date.today())


tickerSymbol = st.sidebar.multiselect('Select Stock Name from Dropdown',('ASIANPAINT.NS', 'UPL.NS', 'ITC.NS', 'NESTLEIND.NS', 'LT.NS', 'HINDUNILVR.NS', 'BRITANNIA.NS', 'POWERGRID.NS', 'RELIANCE.NS', 
	'TATACONSUM.NS', 'CIPLA.NS', 'SBILIFE.NS', 'HCLTECH.NS', 'HDFCLIFE.NS', 'ICICIBANK.NS', 'TITAN.NS', 'JSWSTEEL.NS', 'BHARTIARTL.NS', 
	'ULTRACEMCO.NS', 'INFY.NS', 'BAJAJ-AUTO.NS', 'SHREECEM.NS', 'KOTAKBANK.NS', 'HDFC.NS', 'BAJFINANCE.NS', 'DIVISLAB.NS', 'HDFCBANK.NS',
	 'AXISBANK.NS', 'HEROMOTOCO.NS', 'BAJAJFINSV.NS', 'TCS.NS', 'TECHM.NS', 'MARUTI.NS', 'SUNPHARMA.NS', 'BPCL.NS', 'IOC.NS', 
	 'EICHERMOT.NS', 'ONGC.NS', 'DRREDDY.NS', 'WIPRO.NS', 'NTPC.NS', 'SBIN.NS', 'ADANIPORTS.NS', 'GRASIM.NS', 'INDUSINDBK.NS', 
	 'HINDALCO.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'COALINDIA.NS'),default=['ASIANPAINT.NS', 'UPL.NS', 'ITC.NS', 'NESTLEIND.NS','SBIN.NS'])


dict_list = {}

for ts in tickerSymbol:
	tickerData=yf.Ticker(ts)
	tickerDF=tickerData.history(interval="1d", start=d3-dt.timedelta(100), end=d3)
	raw_cp=tickerDF.Close
	filtered_cp1=pd.DataFrame(raw_cp)
	rest_cp=filtered_cp1.reset_index()
	final_cp=rest_cp['Close']

	dict_list[ts]=final_cp


df=pd.DataFrame(dict_list)

corrMatrix = df.corr()
fig, ax = plt.subplots()
sns.heatmap(corrMatrix, ax=ax, annot=True,linewidths=.5, fmt=".1%")
ax.set_xticklabels(ax.get_xmajorticklabels(), fontsize = 7)
ax.set_yticklabels(ax.get_ymajorticklabels(), fontsize = 7)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)

st.write(fig)
