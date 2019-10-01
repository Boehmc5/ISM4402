#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Christopher Boehm
#9/30/2019

#Import Pandas
import pandas as pd

#Create and load the data frame
Location = "C:\Users\chris\Documents\Python\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()

# Create the bin dividers
score = [0,80,100]
# Create names for the  groups
group_names = ['Fail','Pass']

#Assigning bins
df['lettergrade'] = pd.cut(df['grade'], score, labels=group_names)
df.head()

