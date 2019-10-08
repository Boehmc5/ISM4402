#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Christopher Boehm
#10/7/2019

import pandas as pd

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades = [76, 95, 77, 78, 99]
bsdegrees = [1, 1, 0, 0, 1]
msdegrees = [2, 1, 0, 0, 0]
phddegrees = [0, 1, 0, 0, 0]

GradeList = zip(names, grades, bsdegrees, msdegrees, phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades', 'BS', 'MS', 'PhD'])


# In[9]:


df.count()


# In[10]:


df.mean()


# In[11]:


df.std()


# In[12]:


df.min()


# In[13]:


df.max()


# In[14]:


df.quantile(.25)


# In[15]:


df.quantile(.5)


# In[16]:


df.quantile(.75)


# In[ ]:




