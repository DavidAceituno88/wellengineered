#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime


# In[2]:


df = pd.read_excel('C:\\Users\\David\\Downloads\\Phase 3\\framing_tbl.xlsx')


# In[3]:


df.head()


# In[4]:


df['date_clean'] = pd.to_datetime(df['Date'], errors='coerce')


# In[5]:


df.head()


# In[6]:


print(df.dtypes)


# In[7]:


df.head()
dft=df
dft.head()


# In[8]:


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


# In[9]:


dft.dropna(subset=['hour_column'], inplace=True)


# In[10]:


dft.head()


# In[11]:


hours_day=dft.groupby('date_clean')['hour_column'].sum()


# In[12]:


hours_day.plot(kind='bar')


# In[13]:


sns.barplot(x='date_clean', y='hour_column', hue='Employee', data=dft)


# In[14]:


# Pivot the DataFrame to have days as index and employees as columns
pivot_df = df.pivot_table(index='date_clean', columns='Employee', values='hour_column', aggfunc='sum')

plt.figure(figsize=(10, 8))
pivot_df.plot(kind='bar', stacked=True)
plt.xticks(range(0, 100, 3)) 
plt.show()


# In[15]:


unique_values = df['Description'].unique()
print(unique_values)


# In[45]:


df['week'] = df['date_clean'].dt.strftime('%Y-%U')


# In[46]:


df['week'].unique()


# In[47]:


pivot_df = df.pivot_table(index='week', columns='Employee', values='hour_column', aggfunc='sum')

plt.figure(figsize=(10, 8))
pivot_df.plot(kind='bar', stacked=True)
plt.show()


# In[ ]:





# In[ ]:




