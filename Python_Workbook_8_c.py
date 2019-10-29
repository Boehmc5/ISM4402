#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Christopher Boehm

import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

df.plot.scatter(x='hours', y='grade')


# In[ ]:




