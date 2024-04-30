#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# In[2]:


get_ipython().system('pip install yfinance==0.1.67')
get_ipython().system('mamba install bs4==4.10.0 -y')


# In[3]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[4]:


import yfinance as yf


# In[5]:


tsla = yf.Ticker('TSLA')


# In[6]:


tesla_data = tsla.history(period="max")


# In[7]:


tesla_data.reset_index(inplace=True)


# In[8]:


print(tesla_data.head())


# In[9]:


gme = yf.Ticker('GME')


# In[10]:


gme_data = gme.history(period="max")


# In[11]:


gme_data.reset_index(inplace=True)


# In[12]:


print(gme_data.head())


# In[13]:


import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"


# In[14]:


data  = requests.get(url).text
print(data)


# In[15]:


soup = BeautifulSoup(data, 'html5lib')


# In[16]:


tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    
    
    # Finally we append the data of each row to the table
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue":revenue}, ignore_index=True)   


# In[17]:


tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")


# In[18]:


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[19]:


tesla_revenue.tail()


# In[20]:



url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'


# In[21]:


data1  = requests.get(url).text
print(data1)


# In[22]:


soup1 = BeautifulSoup(data1, 'html5lib')


# In[23]:


from bs4 import BeautifulSoup


# In[24]:


gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup1.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    
    
    # Finally we append the data of each row to the table
    gme_revenue = gme_revenue.append({"Date": date, "Revenue":revenue}, ignore_index=True)   


# In[33]:


gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")


# In[34]:


gme_revenue.dropna(inplace=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]


# In[35]:


gme_revenue.tail()


# In[26]:


pip install ipykernel


# In[27]:


pip install --upgrade nbformat


# In[28]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[29]:


get_ipython().system('pip install nbformat>=4.2.0')


# In[30]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[31]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[36]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




