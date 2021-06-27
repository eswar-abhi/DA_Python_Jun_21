#!/usr/bin/env python
# coding: utf-8

# # Project_titanic

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Data Operations Task

# #### Q. Import the Titianic Dataset and Display the Head of the Dataset

# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/thecodescholar/DA_Python_Jun_21/main/Dataset/titanicDataset.csv', ) 
df.head()


# #### Q. Show the Statistics of dataframe

# In[3]:


df.describe()


# #### Q. Display last 3 columns

# In[4]:


d = pd.read_csv('https://raw.githubusercontent.com/thecodescholar/DA_Python_Jun_21/main/Dataset/titanicDataset.csv',usecols= ["Age", "Fare", "Embarked"] ) 
d.head()


# #### Q. Show Unique values in Embarked

# In[5]:


df.Embarked.unique()


# ## Visualization Task

# #### Q. Draw histogram for Age, using Matplotlib

# In[6]:


plt.hist(data = df, x = 'Age')


# #### Q. Draw countplot for Sex, using Seaborn

# In[7]:


sb.countplot(data = df, x ='Sex')


# #### Q. Make a Pie Chart of Corona Cases by taking numbers list as [500000, 1800000, 1200000] and labels list as ["Deaths", "Total Cases", "Cured"]

# In[8]:


Cases = [500000, 1800000, 1200000]
labels = ["Deaths", "Total Cases", 'Cured']
plt.pie(Cases, labels = labels);


# ### Great Job
# 
# ## All the Best
# 
# # THE CODE SCHOLAR
