#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime


# In[3]:


df = pd.read_excel('C:\\Users\\David\\Downloads\\Phase 3\\cladding_siding_windows_doors_tbl.xlsx')


# In[4]:


df.head()


# In[5]:


df['date_clean'] = pd.to_datetime(df['Date'], errors='coerce')


# In[6]:


df.head()


# In[7]:


print(df.dtypes)


# In[8]:


df.head()
dft=df
dft.head()


# In[9]:


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


# In[10]:


dft.dropna(subset=['hour_column'], inplace=True)


# In[11]:


dft.head()


# In[12]:


hours_day=dft.groupby('date_clean')['hour_column'].sum()


# In[13]:


hours_day.plot(kind='bar')


# In[14]:


sns.barplot(x='date_clean', y='hour_column', hue='Employee', data=dft)


# In[15]:


column_length = len(df['date_clean'])

# Pivot the DataFrame to have days as index and employees as columns
pivot_df = df.pivot_table(index='date_clean', columns='Employee', values='hour_column', aggfunc='sum')
plt.figure(figsize=(20,20))
pivot_df.plot(kind='bar', stacked=True,width=.5, align='center')

plt.xticks(range(0, 100, 3)) 
plt.show


# In[16]:


unique_values = df['Description'].unique()
print(unique_values)


# In[17]:


df['week'] = df['date_clean'].dt.strftime('%Y-%U')


# In[23]:


##Calculate times and sqf per hour and week 
hours = df['hour_column'].sum()
week_df = df[df['hour_column'] != 0]
weeks = len(set(week_df['week']))

#Calculate total sqf framed between walls and roof
sqf_roof =4,140.5
sqf_walls = 3584
sqf_total = sqf_roof = sqf_walls

sqf_hour = sqf_walls / hours
sqf_week = round(sqf_total/weeks,2)
avg_hours_week = round(hours/weeks,2)

#Plot
pivot_df = df.pivot_table(index='week', columns='Employee', values='hour_column', aggfunc='sum')

plt.figure(figsize=(10, 8))
pivot_df.plot(kind='bar', stacked=True)
plt.ylabel('Hours worked')
plt.title('Hours worked weekly')
plt.text(-1, -60,f'The Cladding, siding, windows,doors phase took {hours} hours or {weeks} weeks')
plt.text(-1, -52,f'{sqf_total}sqf where done in {weeks} weeks, wich means an average of {sqf_week}sqf week')
plt.show()


# In[25]:


workers_per_week = week_df.groupby('week')['Employee'].nunique()
week_by_workers = workers_per_week.groupby(workers_per_week).count()
plt.figure(figsize=(8, 6))
week_by_workers.plot(kind='pie', autopct='%1.1f%%')
plt.legend(title='Number of Workers', loc='upper right')
plt.title("Distribution of Weeks by Number of Workers")
plt.ylabel('')
plt.text(0, -1.2,'Most of the time there were between 2 and 4 workers completing this task',fontsize=12, ha='center')


# In[ ]:




