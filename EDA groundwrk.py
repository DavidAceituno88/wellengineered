#!/usr/bin/env python
# coding: utf-8

# In[144]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime


# In[145]:


df = pd.read_excel('C:\\Users\\David\\Downloads\\Phase 3\\groundwrk_tbl.xlsx')


# In[146]:


df.head()


# In[147]:


df['date_clean'] = pd.to_datetime(df['Date'], errors='coerce')


# In[148]:


df.head()


# In[149]:


print(df.dtypes)


# In[152]:


df.head()
dft=df
dft.head()


# In[153]:


def convert_to_hour(time_str):
    if isinstance(time_str, str):
        try:
            time_format = "%H:%M"
            time_obj = datetime.strptime(time_str, time_format)
            return time_obj.hour
        except ValueError:
            return None  # or any other value you prefer for invalid inputs
    else:
        return None 
dft['hour_column'] = df['Hours'].apply(convert_to_hour)
dft.head()


# In[154]:


dft.dropna(subset=['hour_column'], inplace=True)


# In[155]:


dft.head()


# In[170]:


hours_day=dft.groupby('date_clean')['hour_column'].sum()


# In[171]:


hours_day.plot(kind='bar')


# In[181]:


sns.barplot(x='date_clean', y='hour_column', hue='Employee', data=dft)


# In[184]:


# Pivot the DataFrame to have days as index and employees as columns
pivot_df = df.pivot_table(index='date_clean', columns='Employee', values='hour_column', aggfunc='sum')
pivot_df.plot(kind='bar', stacked=True)


# In[ ]:




