#!/usr/bin/env python
# coding: utf-8

# # Apple vs Samsung Stock Closing Price Comparison

# In[1]:


pip install finance-datareader # library download for finance database in python


# In[7]:


import FinanceDataReader as fdr


# In[18]:


samsung = fdr.DataReader('005930') # samsung stock ticker = 005930
samsung_first_date = str(samsung.index[0])
apple = fdr.DataReader('AAPL', samsung_first_date) # apple stock ticker = AAPL
samsung


# In[19]:


apple


# In[14]:


# NaN Boolean = False - checking to see if there exists any false values 
# Missing data check 
samsung_isna = samsung.isna().sum()
apple_isna = apple.isna().sum()


# In[16]:


samsung_isna


# In[17]:


apple_isna


# In[5]:


samsung = samsung.fillna(0)  # 0 is true value, fills the 1 missing value with 0 thus making it true 
samsung


# ## Stock Data Visualization

# In[21]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


# In[58]:


plt.figure(figsize=(15,10))
plt.plot(samsung["Close"], label = 'SAMSUNG', color = "red")   # Koreans use Won
plt.plot(apple["Close"], label = 'APPLE', color = "blue")   # Apples uses USD    1 USD = 1000 Won 
plt.legend(fontsize = 15)
plt.show()


# In[83]:


#conversion to make apple stocks match samsung price since Korea uses Won
sam_exp = (samsung["Close"] / samsung["Close"][samsung_first_date])
aapl_exp = (apple["Close"] / apple["Close"][samsung_first_date])
plt.figure(figsize=(15,10))
plt.title("Samsung vs Apple Stock Closing Price Differentials", fontsize = 30, x=0.5, y=1.02, weight = "bold")
plt.plot(sam_exp, label = 'SAMSUNG', color = "red")
plt.plot(aapl_exp, label = 'APPLE', color = "blue")
x1 = plt.xlabel('Year (1999-2024)', fontsize = 20, color = "blue", weight = "bold")
y1 = plt.ylabel('Daily Closing Price vs. Initial Closing Price', fontsize = 20, color = "red", weight = "bold")
plt.ylim(0,550)
plt.legend(fontsize = 16)
plt.grid()
plt.show()


# ### USD to Korean Won exchange Rate

# In[65]:


usd_krw = fdr.DataReader('USD/KRW', '2023-03-15', '2023-08-15')   # USD/KRW -> conversion of tickers built in function
usd_krw.tail(100)


# In[63]:


plt.figure(figsize=(12,6))
plt.plot(usd_krw.index, usd_krw['Close'])
plt.title("USD/KRW Exchange Rate (2022-03-29 to 2022-08-15)")
plt.xlabel('Date')
plt.ylabel('Exchange Rate (USD/KRW)')
plt.grid()
plt.show()


# In[ ]:




