#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Christopher Boehm
#Workbook Assignment 2A
#9/16/2019

#import function
import pandas as pd
import numpy as np
import glob

#creating a data frame
all_data = pd.DataFrame()

#loops through the folder and returns all xls files
for f in glob.glob("C:\Users\chris\Documents\Python\datasets\weekly_call_data\weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()

