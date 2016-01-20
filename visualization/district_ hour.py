
# coding: utf-8

# In[19]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# In[2]:

import re 
from patsy import dmatrices


# In[3]:

train = pd.read_csv('train.csv', header = 0)
test = pd.read_csv('test.csv', header = 0)


# In[4]:

names = sorted(train.Category.unique())


# In[8]:

#generate features from train dataset, get hour, minute
train["Dates"]=pd.to_datetime(train["Dates"])


# In[9]:

train["hour"]=train["Dates"].dt.hour
train["minute"]=train["Dates"].dt.minute


# In[11]:

train["PdDistrict"].unique()


# In[12]:

district_hour = train[["PdDistrict", "hour", "Category"]].groupby(["PdDistrict", "hour"]).count().reset_index()


# In[13]:

district_hour_table = district_hour.pivot(index = "hour", columns = "PdDistrict", values = "Category")


# In[20]:

get_ipython().magic(u'matplotlib inline')
district_hour_table.interpolate().plot(title = 'count of crimes by hour', figsize = (12, 9))
plt.savefig('district and hour.png')

