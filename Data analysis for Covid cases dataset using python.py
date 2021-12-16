#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


covid=pd.read_csv(r'D:\covid_data_pyhton.csv')


# In[3]:


covid.head(3)


# # Data analysis using Python for covid cases dataset.

# Null values identification

# In[5]:


covid.isnull().sum()


# In[6]:


import seaborn as sns;
import matplotlib.pyplot as plt;


# In[12]:


sns.heatmap(covid.isnull())
plt.show()


# In[10]:


covid.count()


# q1.Show the confirm case,death case,recover case according to region wise. 

# In[13]:


covid.head(2)


# In[15]:


covid.groupby('Region').sum().head(5)


# In[25]:


covid.groupby('Region') ['Confirmed'].sum().sort_values(ascending=False).head(5)


# In[26]:


covid.groupby('Region')['Deaths'].sum().sort_values(ascending=False)


# In[27]:


covid.groupby('Region').Deaths.sum()


# q2.In which region maxium confirmed cases were recorded?
# 

# In[29]:


covid.groupby('Region')['Confirmed'].sum().sort_values(ascending=False)


# q3.In which Region lowest deaths cases recorded?

# In[30]:


covid.groupby('Region')['Deaths'].sum().sort_values(ascending=True)


# q4.How many confirmed,deaths,recovery cases recorded in india till 29 april 2020?

# In[31]:


covid[covid['Region']=='India']


# q5.Sort the table according to highest confirmed cases?

# In[32]:


covid.sort_values(by=['Confirmed'],ascending=False)


# q6.sort the table according to lowest death cases?

# In[33]:


covid.sort_values(by=['Deaths'],ascending=True)


# q7.delete the records where confirmed cases are less than 10.

# In[36]:


covid[(covid['Confirmed']<10)].shape


# In[37]:


covid[(covid['Confirmed']<10)]


# In[35]:


covid[~(covid['Confirmed']<10)]


# In[ ]:




