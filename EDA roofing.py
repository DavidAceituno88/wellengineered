#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime


# In[23]:


df = pd.read_excel('C:\\Users\\David\\Downloads\\Phase 3\\roofing_tbl.xlsx')


# In[24]:


df.head()


# In[25]:


df['date_clean'] = pd.to_datetime(df['Date'], errors='coerce')


# In[26]:


df.head()


# In[27]:


print(df.dtypes)


# In[28]:


df.head()
dft=df
dft.head()


# In[29]:


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


# In[30]:


dft.dropna(subset=['hour_column'], inplace=True)


# In[31]:


dft.head()


# In[32]:


hours_day=dft.groupby('date_clean')['hour_column'].sum()


# In[33]:


hours_day.plot(kind='bar')


# In[34]:


sns.barplot(x='date_clean', y='hour_column', hue='Employee', data=dft)


# In[36]:


# Pivot the DataFrame to have days as index and employees as columns
pivot_df = df.pivot_table(index='date_clean', columns='Employee', values='hour_column', aggfunc='sum')
pivot_df.plot(kind='bar', stacked=True)


# In[43]:


df['week'] = df['date_clean'].dt.strftime('%Y-%U')

##Calculate times and sqf per hour and week 
hours = df['hour_column'].sum()
week_df = df[df['hour_column'] != 0]
weeks = len(set(week_df['week']))


roof_sq_ft = 4929



sqf_week = round(roof_sq_ft/weeks,2)
avg_hours_week = round(hours/weeks,2)

#Plot
pivot_df = df.pivot_table(index='week', columns='Employee', values='hour_column', aggfunc='sum')

plt.figure(figsize=(10, 8))
pivot_df.plot(kind='bar', stacked=True)
plt.ylabel('Hours worked')
plt.title('Hours worked weekly')
plt.text(-1, -44,f'The Roofing phase took {hours} hours or {weeks} weeks')
plt.text(-1, -52,f'{roof_sq_ft}sqft of foundation was done in {weeks} weeks, wich means an average of {sqf_week}ft per week')
plt.show()


# In[44]:


workers_per_week = week_df.groupby('date_clean')['Employee'].nunique()
week_by_workers = workers_per_week.groupby(workers_per_week).count()
plt.figure(figsize=(9, 7))
week_by_workers.plot(kind='pie', autopct='%1.1f%%')
plt.legend(title='Number of Workers', loc='upper right')
plt.title("Distribution of Weeks by Number of Workers")
plt.ylabel('')
plt.text(0, -1.2,'Most of the time there were 1 to 2 workers completing this task',fontsize=12, ha='center')


# In[ ]:




