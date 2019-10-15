#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location="Documents\BI - Python\datasets\gradedata.csv"
df=pd.read_csv(Location)
df.head()

df=df.sort_values(by=['lname','age','grade'],
                 ascending=[True,True,True])
df.head.()

