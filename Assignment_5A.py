#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Christopher Boehm
#10/7/2019

import pandas as pd
import numpy as np

Location = "Documents\BI - Python\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.tail()

df.take(np.random.permutation(len(df))[:500])

