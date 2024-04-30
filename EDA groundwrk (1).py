#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime


# In[2]:


df = pd.read_excel('C:\\Users\\David\\Downloads\\Phase 3\\groundwrk_tbl.xlsx')


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


# In[17]:


# Pivot the DataFrame to have days as index and employees as columns
pivot_df = df.pivot_table(index='date_clean', columns='Employee', values='hour_column', aggfunc='sum')
pivot_df.plot(kind='bar', stacked=True)


# In[23]:


df['week'] = df['date_clean'].dt.strftime('%Y-%U')

##Calculate times and sqf per hour and week 
hours = df['hour_column'].sum()
week_df = df[df['hour_column'] != 0]
weeks = len(set(week_df['week']))


foundation_linear_ft = 310



lf_week = round(foundation_linear_ft/weeks,2)
avg_hours_week = round(hours/weeks,2)

#Plot
pivot_df = df.pivot_table(index='week', columns='Employee', values='hour_column', aggfunc='sum')

plt.figure(figsize=(10, 8))
pivot_df.plot(kind='bar', stacked=True)
plt.ylabel('Hours worked')
plt.title('Hours worked weekly')
plt.text(-1, -20,f'The foundation phase took {hours} hours or {weeks} weeks')
plt.text(-1, -24,f'{foundation_linear_ft} linear ft of foundation was done in {weeks} weeks, wich means an average of {lf_week}ft per week')
plt.show()


# In[25]:


workers_per_week = week_df.groupby('date_clean')['Employee'].nunique()
week_by_workers = workers_per_week.groupby(workers_per_week).count()
plt.figure(figsize=(9, 7))
week_by_workers.plot(kind='pie', autopct='%1.1f%%')
plt.legend(title='Number of Workers', loc='upper right')
plt.title("Distribution of Weeks by Number of Workers")
plt.ylabel('')
plt.text(0, -1.2,'Most of the time there were 1 to 2 workers completing this task',fontsize=12, ha='center')


# In[ ]:




