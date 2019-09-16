#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Christopher Boehm
#Workbook Assignment 2B
#9/16/2019

#import function
import pandas as pd
from sqlalchemy import create_engine

# Connect to sqlite db
db_file = r'C:\Users\chris\Documents\Python\datasets\gradedata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))
sql = 'SELECT * from test where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df.head()


# In[ ]:




