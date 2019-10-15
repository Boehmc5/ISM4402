#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
Location = "Documents\BI - Python\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[11]:


def gen_to_num(x):
    if x == 'female':
        return 1
    if x == 'male':
        return 0


# In[12]:


df['gender_val'] = df['gender'].apply(gen_to_num)
df.tail()


# In[13]:


import statsmodels.formula.api as sm
results = sm.ols(formula='grade ~ age + exercise + hours + gender_val',data=df).fit()
results.summary()


# In[14]:


import statsmodels.formula.api as sm
results = sm.ols(formula='grade ~ exercise + hours + gender_val',data=df).fit()
results.summary()

