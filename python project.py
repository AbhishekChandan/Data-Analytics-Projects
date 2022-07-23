#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data=pd.read_csv("Weather Data.csv")
data


# In[63]:


data.dtypes


# In[ ]:





# In[ ]:





# In[14]:


data.head(6)


# In[16]:


data.index


# In[19]:


data.columns


# In[1]:


data.dtypes


# In[ ]:





# In[25]:


data['Weather'].unique()


# In[26]:


data.nunique()


# In[38]:


data['Temp_C'].nunique()
#data['Temp_C'].unique()


# In[64]:


data['Temp_C'].unique()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


data.count()


# In[9]:


data['Weather'].value_counts()


# In[11]:


data['Weather'].unique()


# In[65]:


data[data['Weather']=='Cloudy']
#data[data["Weather"].str.contains("Snow")]


# In[66]:


data[data["Weather"].str.contains("Snow")]


# In[ ]:





# In[31]:


data
data["Wind Speed_km/hWind Speed_km/h"].counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


data.info()


# In[ ]:





# In[ ]:





# In[7]:


data.nunique()


# In[12]:


data["Wind Speed_km/h"].value_counts()


# In[13]:


data.nunique()


# In[15]:


data["Weather"].unique()


# In[17]:


data["Weather"].value_counts()


# In[43]:


data[data["Weather"]=="Clear"]


# In[ ]:





# In[ ]:





# In[25]:


data.groupby('Weather').get_group('Clear')


# In[30]:


data.columns


# In[67]:


data[data["Wind Speed_km/h"]==4]


# In[ ]:





# In[45]:


data.isnull().sum()


# In[18]:


data.notnull().sum()


# In[20]:


data["Weather"].value_counts()


# In[ ]:





# In[ ]:





# In[50]:


data.rename(columns={"Weather":"Weather Condiion"},inplace=True)


# In[51]:


data


# In[ ]:


visibility


# In[53]:


data.Visibility_km.mean()


# In[69]:


data["Press_kPa"].std()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[61]:


data
data["Rel Hum_%"].var()


# In[21]:


data


# In[22]:


data


# In[ ]:





# In[17]:


data["Weather Condiion"].value_counts()


# In[39]:


data


# In[43]:


data[(data["Wind Speed_km/h"]>24) & (data['Visibility_km']==25)]


# In[44]:


data


# In[51]:


data.groupby('Weather').mean()


# In[52]:


data.groupby('Weather').max()


# In[53]:


data.groupby('Weather').min()


# In[54]:


data.head(2)


# In[56]:


data[data['Weather']=='Fog']


# In[57]:


data["Weather"].unique()


# In[62]:


data[(data['Weather']=='Clear') & (data['Rel Hum_%']>50)]


# In[ ]:





# In[ ]:





# In[ ]:


data[(data['Weather']=='Clear') | (data['Visibility_km']>40)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


data["Weather Condiion"].unique()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


data
data["Weather Condiion"].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




