
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


# In[36]:

train["Intersection"]=[0 if re.search("/", i ) == None else 1 for i in train["Address"]]


# In[38]:

train["Night"]=[1 if i < 6 or i >22 else 0 for i in train.hour]


# In[40]:

train["Week"]=[1 if i == "Sunday" or i == "Saturday" else 0 for i in train["DayOfWeek"]]


# In[64]:

formula ='C(Category) ~ C(PdDistrict)+X+Y+hour+minute+C(Intersection)+C(Night)+C(Week)' 


# In[65]:

y, x = dmatrices(formula, data = train, return_type = 'dataframe')


# In[67]:

import statsmodels.api as sm


# In[86]:

submit = {}
for i in range(len(names)):
    model = sm.Logit(y[[i]],x)
    res = model.fit()
    ypred = res.predict(x)
    submit[names[i]] = ypred


# In[88]:

type(submit)


# In[ ]:

formula ='y[[1]] ~ C(PdDistrict)+X+Y+hour+minute+Intersection+Night+Week' 


# In[ ]:

mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
mod1.summary()


# In[70]:

submit = pd.read_csv('sampleSubmission.csv')


# In[71]:

submit


# In[12]:

test.shape


# In[ ]:



