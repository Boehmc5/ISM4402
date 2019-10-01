#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Christopher Boehm
#9/30/2019

#import packages
import pandas as pd
import numpy as np

#Create and load dataframe
Location = "C:\Users\chris\Documents\Python\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()

#Create a timemgmt column
df['timemgmt'] = np.where((df['exercise'] > 3)
                               & (df['hours'] > 17),'Busy Studying', 'Available')
df.tail(10)


# In[ ]:




