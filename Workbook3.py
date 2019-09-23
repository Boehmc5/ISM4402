#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Christopher Boehm
#Workbook 3

import pandas as pd
#list of names and grades
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])
#filters out if the grade is without a certian range
df.loc[(df['Grades'] >= 100,'Grades')] = 100
df.loc[(df['Grades'] <= 0,'Grades')] = 0
df


# In[ ]:




