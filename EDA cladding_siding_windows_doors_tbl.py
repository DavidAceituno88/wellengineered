#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime


# In[2]:


df = pd.read_excel('C:\\Users\\David\\Downloads\\Phase 3\\cladding_siding_windows_doors_tbl.xlsx')


# In[3]:


df.head()


# In[4]:


df['date_clean'] = pd.to_datetime(df['Date'], errors='coerce')


# In[5]:


df.head()


# In[6]:


print(df.dtypes)


# In[9]:


df.head()
dft=df
dft.head()


# In[10]:


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


# In[11]:


dft.dropna(subset=['hour_column'], inplace=True)


# In[12]:


dft.head()


# In[13]:


hours_day=dft.groupby('date_clean')['hour_column'].sum()


# In[14]:


hours_day.plot(kind='bar')


# In[15]:


sns.barplot(x='date_clean', y='hour_column', hue='Employee', data=dft)


# In[31]:


column_length = len(df['date_clean'])

# Pivot the DataFrame to have days as index and employees as columns
pivot_df = df.pivot_table(index='date_clean', columns='Employee', values='hour_column', aggfunc='sum')
plt.figure(figsize=(20,20))
pivot_df.plot(kind='bar', stacked=True,width=.5, align='center')
for i in range(5, column_length + 1, 5):
    plt.axvline(x=i + 0.5, color='red', linestyle='--')
plt.xticks(range(0, 100, 3)) 
plt.show


# In[21]:


unique_values = df['Description'].unique()
print(unique_values)


# In[ ]:




