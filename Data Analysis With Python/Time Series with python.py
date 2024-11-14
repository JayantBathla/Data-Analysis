#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


stock_data = yf.download('AAPL', start = '2024-01-01')
stock_data.head(10)


# In[73]:


stock_data.describe()


# In[2]:


plt.figure(figsize = (12,6))
plt.plot(stock_data.index, stock_data['Close'], label = 'Close Price')
plt.title("APPLE Stock Prices Over Time")
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()


# In[3]:


## Classical Time Decomposition


# In[4]:


from statsmodels.tsa.seasonal import seasonal_decompose

decompose_additive = seasonal_decompose(stock_data['Close'], model = 'additive', period = 30)


# In[5]:


trend_additive = decompose_additive.trend
seasonal_additive = decompose_additive.seasonal
residual_additive = decompose_additive.resid


# In[6]:


plt.figure(figsize = (14,10))
plt.subplot(411)
plt.plot(stock_data['Close'], label = 'Original')
plt.legend(loc = 'upper left')
plt.subplot(412)
plt.plot(trend_additive, label = 'Trend')
plt.legend(loc = 'upper left')
plt.subplot(413)
plt.plot(seasonal_additive, label = 'Seasonal')
plt.legend(loc = 'upper left')
plt.subplot(414)
plt.plot(residual_additive, label = 'Residual')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()


# In[7]:


## STL Decomposition


# In[8]:


from statsmodels.tsa.seasonal import STL

stl = STL(stock_data['Close'],  period = 30)


# In[9]:


result= stl.fit()


# In[10]:


plt.figure(figsize = (14,10))
plt.subplot(411)
plt.plot(result.observed, label = 'Original', color = 'red')
plt.legend(loc = 'upper left')
plt.subplot(412)
plt.plot(result.trend, label = 'Trend',color = 'red')
plt.legend(loc = 'upper left')
plt.subplot(413)
plt.plot(result.seasonal, label = 'Seasonal', color = 'red')
plt.legend(loc = 'upper left')
plt.subplot(414)
plt.plot(result.resid, label = 'Residual', color = 'red')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()


# In[59]:


from statsmodels.tsa.stattools import adfuller
adf_test = adfuller(stock_data['Close'])

print("ADF test result:")
print(f'ADF Statistic: {round(adf_test[0],3)}')
print(f'p-value: {round(adf_test[1],3)}')
print("Critical Values:")
for key, value in adf_test[4].items():
    print(f'   {key}: {round(value,3)}')


# In[12]:


from statsmodels.tsa.stattools import kpss
kpss_test = kpss(stock_data['Close'], regression = 'ct') # c for constant level stationarity, ct for trend

print("KPSS test result:")
print(f'kpss Statistic: {round(kpss_test[0],3)}')
print(f'p-value: {kpss_test[1]}')
print("Critical Values:")
for key, value in kpss_test[3].items():
    print(f'   {key}: {round(value,3)}')


# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp


# In[14]:


np.random.seed(0)
n = 500

strict_series = np.random.normal(0,1,n)
non_strict = np.concatenate([np.random.normal(0,1,n//2), np.random.normal(0,1,n//2)])
     

def ks_test(series):
    split = len(series)//2
    series_first = series[:split]
    series_second= series[split:]
    stat, p_value = ks_2samp(series_first,series_second)
    return stat, p_value
                            
ks_stat_strict, ks_pvalue_strict = ks_test(strict_series)
                            
                            
ks_stat_non_strict, ks_pvalue_non_strict = ks_test(non_strict)
    
plt.figure(figsize = (14,6))
plt.plot(non_strict)


print(ks_stat_non_strict, ks_pvalue_non_strict)
print(ks_stat_strict, ks_pvalue_strict)


# In[15]:


plt.plot(strict_series)


# In[ ]:





# In[ ]:





# # making data stationary

# In[16]:


stock_data


# In[17]:


#kpss and adf test
from statsmodels.tsa.stattools import adfuller


def adf_test(series):
    result = adfuller(series)
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print("Critical Values:")
    for key, value in result[4].items():
        print("Critical value (%s): %.3f" % (key,value))
    
from statsmodels.tsa.stattools import kpss
def kpss_test(series):
    result = kpss(series, regression = 'c')
    print(f'kpss Statistic: {result[0],3}')
    print(f'p-value: {result[1]}')
    print("Critical Values:")
    for key, value in result[3].items():
        print("Critical value (%s): %.3f" % (key,value))


# In[18]:


prices = stock_data['Close']


# In[19]:


adf_test(prices)


# In[20]:


prices


# In[21]:


pricediff = prices.diff()#differencing


# In[22]:


adf_test(pricediff.dropna())


# In[23]:


1.1495281206059632e-25<0.05


# In[24]:


#adf stat> critical value therefore stationary


# In[25]:


# Transformation


# In[26]:


import numpy as np
from scipy import stats


# In[27]:


prices_log = np.log(prices)
prices_power = np.sqrt(prices)
#boxcox requires all positive values
prices_boxcox, lam = stats.boxcox(prices[prices > 0])


# In[28]:


prices_log


# In[29]:


prices_power


# In[30]:


prices_boxcox


# In[31]:


adf_test(prices_log)



# In[32]:


adf_test(prices_power)


# In[33]:


adf_test(prices_boxcox)#any of the transformation steps werent useful for this data, meaning data is not so varied


# In[34]:


# DE-TRENDING


# In[35]:


from scipy import signal
trend= np.polyfit(np.arange(len(prices)), prices ,1)
trend_line = np.polyval(trend ,np.arange(len(prices)))
prices_detrended = prices-trend_line


# In[36]:


prices_detrended


# In[37]:


adf_test(prices_detrended) #this didnt work for this particular data


# In[38]:


plt.plot(np.arange(len(prices)), prices)
plt.plot(np.arange(len(prices)), trend_line)


# In[39]:


window = 12
prices_ma = prices.rolling(window=window).mean()
prices_detrend= prices-prices_ma
prices_detrend = prices_detrend.dropna()


# In[40]:


prices_detrend


# In[41]:


adf_test(prices_detrend) # this worked data is stationary


# In[42]:


plt.plot(np.arange(len(prices)), prices_ma)
plt.plot(np.arange(len(prices)), prices)


# In[43]:


## LASTLY SEASONAL DECOMPOSITION

decomposition = seasonal_decompose(prices, model = 'additive', period = 30)
prices_adjusted= prices / decomposition.seasonal
prices_adjusted = prices_adjusted.dropna()


# In[44]:


adf_test(prices_adjusted)


# In[ ]:





# # Forecasting Models

# In[45]:


#first make data stationary
stock_stationary = stock_data['Close'].diff().dropna()
train_data, test_data = stock_stationary[:-30],stock_stationary[-30:]


# In[46]:


from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import numpy as np


# fit model in training data
model = AutoReg(train_data,lags = 30)
model_fit = model.fit()


#make predictions
prediction = model_fit.predict(start = len(train_data), end = len(train_data)+len(test_data)-1, dynamic = False)

#plot actual vs predicted
plt.figure(figsize= (12,6))
plt.plot(test_data.index, test_data, label = 'Test Data')
plt.plot(test_data.index, prediction,color = 'red',  label = 'Predicted')
plt.legend()
plt.show()

#evaluating model using rmse score

rmse = round(np.sqrt(mean_squared_error(test_data,prediction)),2)
print('RMSE:', rmse)


# In[47]:


## MA MODEL there is no direct function to call ma model but when we keep p,d =0 in arima it becomes ma model 


# In[48]:


from statsmodels.tsa.arima.model import ARIMA

#fitting into model
model = ARIMA(train_data, order = (0,0,30))
model_fit = model.fit()

#making predictions
prediction = model_fit.predict(start = len(train_data), end = len(train_data)+len(test_data)-1, dynamic = False)

#plot actual vs predicted
plt.figure(figsize= (12,6))
plt.plot(test_data.index, test_data, label = 'Test Data')
plt.plot(test_data.index, prediction,color = 'red', linestyle = '--',  label = 'Predicted')
plt.legend()
plt.show()
rmse = round(np.sqrt(mean_squared_error(test_data,prediction)),2)
print('RMSE:', rmse)


# In[49]:


#ARMA in this we will keep d = 0



model = ARIMA(train_data, order = (7,0,7))
model_fit = model.fit()

#making predictions
prediction = model_fit.predict(start = len(train_data), end = len(train_data)+len(test_data)-1, dynamic = False)

#plot actual vs predicted
plt.figure(figsize= (12,6))
plt.plot(test_data.index, test_data, label = 'Test Data')
plt.plot(test_data.index, prediction,color = 'red', linestyle = '--',  label = 'Predicted')
plt.legend()
plt.show()
rmse = round(np.sqrt(mean_squared_error(test_data,prediction)),2)
print('RMSE:', rmse)


# In[50]:


# ARIMA
model = ARIMA(train_data, order = (7,1,7))
model_fit = model.fit()

#making predictions
prediction = model_fit.predict(start = len(train_data), end = len(train_data)+len(test_data)-1, dynamic = False)

#plot actual vs predicted
plt.figure(figsize= (12,6))
plt.plot(test_data.index, test_data, label = 'Test Data')
plt.plot(test_data.index, prediction,color = 'red', linestyle = '--',  label = 'Predicted')
plt.legend()
plt.show()
rmse = round(np.sqrt(mean_squared_error(test_data,prediction)),2)
print('RMSE:', rmse)


# In[51]:


# Sarima Model
from statsmodels.tsa.statespace.sarimax import SARIMAX
p,d,q = 7,1,7
P,D,Q, s=1,1,1,45
model = SARIMAX(train_data, order = (p,d,q), seasonal_order =(P,D,Q,s))
model_fit = model.fit()

#making predictions
prediction = model_fit.predict(start = len(train_data), end = len(train_data)+len(test_data)-1, dynamic = False)

#plot actual vs predicted
plt.figure(figsize= (12,6))
plt.plot(test_data.index, test_data, label = 'Test Data')
plt.plot(test_data.index, prediction,color = 'red', linestyle = '--',  label = 'Predicted')
plt.legend()
plt.show()
rmse = round(np.sqrt(mean_squared_error(test_data,prediction)),2)
print('RMSE:', rmse)


# In[52]:


##VECTOR MODELS
stock_data = yf.download('AAPL', start = '2024-01-01')
stock_data.head(10)


# In[53]:


stock_data1 = yf.download('TSLA', start = '2024-01-01')
stock_data1.head(10)


# In[54]:


stock_data['TSLA_Close'] = stock_data1['Close']
stock_data['AAPL_Close'] = stock_data['Close'].shift()
stock_data.dropna(inplace = True)


from statsmodels.tsa.stattools import grangercausalitytests

#performing granger test
grangercausalitytests(stock_data[['AAPL_Close', 'TSLA_Close']].dropna(), maxlag = [14])
print()


# In[55]:


data = stock_data[['AAPL_Close', 'TSLA_Close']].diff().dropna()
train_data, test_data = data[:-14],data[-14:]


# In[56]:


from statsmodels.tsa.api import VAR, VARMAX
import pandas as pd
model = VAR(train_data)
result = model.fit(maxlags = 7)
pridiction = result.forecast(train_data.values[-result.k_ar:], steps = len(test_data))
pridiction = pd.DataFrame(pridiction, index = test_data.index, columns = test_data.columns)


plt.figure(figsize= (10,6))
plt.plot(test_data.index, test_data['TSLA_Close'], label = 'Actual Price')
plt.plot(test_data.index, pridiction['TSLA_Close'],color = 'red', linestyle = '--',  label = 'Predicted')
plt.legend()
plt.show()
    


# In[57]:


model = VARMAX(train_data, order = (8,14))
result = model.fit()
pridiction = result.predict(start = len(train_data), end = len(train_data)+len(test_data)-1, dynamic = False)



plt.figure(figsize= (10,6))
plt.plot(test_data.index, test_data['TSLA_Close'], label = 'Actual Price')
plt.plot(test_data.index, pridiction['TSLA_Close'],color = 'red', linestyle = '--',  label = 'Predicted')
plt.legend()
plt.show()


# # Smoothing methods

# In[58]:


window_size =20
stock_data['SMA'] = stock_data['Close'].rolling(window=window_size).mean()

weights = np.arange(1, window_size+1)
stock_data['WMA'] = stock_data['Close'].rolling(window_size).apply(lambda prices: np.dot(prices,weights)/weights.sum(), raw = True)
stock_data['EMA']= stock_data['Close'].ewm(span = window_size).mean()

plt.figure(figsize = (10,6))
plt.plot(stock_data['Close'], label = 'close price', color = 'hotpink')
plt.plot(stock_data['SMA'], label = f'SMA{window_size}-day', color = 'red')
plt.plot(stock_data['WMA'], label = f'WMA{window_size}-day', color = 'green')
plt.plot(stock_data['EMA'], label = f'EMA{window_size}-day', color = 'blue')
plt.legend()
plt.grid()
plt.show()




# In[60]:


#ACF PACF


# In[62]:


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.figure(figsize = (12,6))



plt.subplot(1,2,1)
plot_acf(stock_data['Close'].diff().diff().dropna(), ax = plt.gca(), lags = 50)
plt.title('ACF')


plt.subplot(1,2,2)
plot_pacf(stock_data['Close'].diff().diff().dropna(), ax = plt.gca(), lags = 50, method = 'ywm')
plt.title('PACF')

plt.tight_layout()
plt.show()


# In[63]:


# acf cuts off at 1 and pacf cuts of at 8, p = 8, q =1


# In[64]:


#model evaluation techniques


# In[65]:


stock_stationary = stock_data['Close'].diff().dropna()
train_data, test_data = stock_stationary[:-30],stock_stationary[-30:]


# In[66]:


# fit model in training data
model = AutoReg(train_data,lags = 30)
model_fit = model.fit()


#make predictions
prediction = model_fit.predict(start = len(train_data), end = len(train_data)+len(test_data)-1, dynamic = False)


# In[72]:


from sklearn.metrics import mean_absolute_error, mean_squared_error


mae = mean_absolute_error(test_data, prediction)
print(mae)

mse = mean_squared_error(test_data, prediction)
print(mse)


rmse = np.sqrt(mse)
print(rmse)



mape = np.mean(np.abs((list(test_data)- prediction)/list(test_data))) *100
print(mape)



aic = model_fit.aic
bic = model_fit.bic


print(aic)
print(bic)


# In[ ]:




