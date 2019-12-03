#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

Location = "Documents\BI - Python\datasets\dataaxis.csv"
df = pd.read_csv(Location)
df.head()


# In[9]:


df['Cars Sold'].mean()


# In[10]:


df['Cars Sold'].max()


# In[11]:


df['Cars Sold'].min()


# In[12]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[13]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[14]:


df['Years Experience'].mean()


# In[16]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[15]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[33]:


pd.pivot_table(df, values=['Hours Worked'], index=['Gender'])


# In[41]:


pd.pivot_table(df, values=['Years Experience'], index=['Lname', 'Fname'])


# In[42]:


pd.pivot_table(df, values=['Hours Worked'], index=['SalesTraining'])


# In[ ]:




