#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[5]:


df = pd.read_csv("starbucks.csv")
# To display the top 5 rows 
df.head(5)


# In[ ]:





# In[4]:


df.tail(5)  # To display the botton 5 rows


# In[19]:


df.dtypes


# In[20]:


df = df.drop(['Cholesterol (mg)',' Dietary Fibre (g)'], axis=1)
df.head(5)


# In[8]:


df = df.rename(columns={"Beverage_category":"Bevg_category","Beverage":"Bevg","Beverage_prep":"Bevg_prep","Sugars (g)":"Sugars" })
df.head(5)


# In[7]:


df.shape


# In[8]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)


# In[9]:


df.count()      # Used to count the number of rows


# In[10]:


df = df.drop_duplicates()
df.head(5)


# In[11]:


df.count()


# In[12]:


print(df.isnull().sum())


# In[13]:


df = df.dropna()    # Dropping the missing values.
df.count()


# In[14]:


print(df.isnull().sum())   # After dropping the values


# In[ ]:





# In[21]:


sns.boxplot(x=df['Calories'])


# In[27]:


sns.boxplot(x=df['Cholesterol (mg)'])


# In[28]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[29]:


df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape


# In[9]:


df.Bevg.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Starbucks coffee")
plt.ylabel('Bevg_prep')
plt.xlabel('Bevg');


# In[32]:


plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# In[44]:


fig, ax = plt.subplots(figsize=(19,10))
ax.scatter( df['Bevg_prep'],df['Calories'],)
ax.set_xlabel('Bevg_prep')
ax.set_ylabel('Calories')
plt.show()


# In[ ]:




