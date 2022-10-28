#!/usr/bin/env python
# coding: utf-8

# # `BERCHMANS KEVIN S`
# 

# ## Department of Data Science - Data and Visual Analytics Lab

# 
# ## `Red Wine Quality Data Analytics using NumPy Part-I`

# In[1]:


'''
wine quality dataset 11 input features and 1 output feature 

1- fixed acidity
2- volatile acidity
3-citric acid
4-residual sugar
5-chlorides
6-free sulfurdioxide
7- total sulfur dioxide
8- density
9- pH
10- sulphates
11- alcohol output variable(based on sensory data): 
12- quality(score between 0 and 10)'''


# ### import modules for numpy

# In[2]:


import numpy as np


# In[3]:


wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)


# In[4]:


wines


# #### What is its size?

# In[5]:


np.shape(wines)


# #### How many wine data rows here? 
# 

# In[6]:


np.shape(wines)[0]


# #### How many wine data columns here? 

# In[7]:


np.shape(wines)[1]


# #### How many dimensions? 

# In[8]:


np.ndim(wines)


# #### What is the type of wines? 
# 

# In[9]:


type(wines)


# #### What is the data type of wines data? 

# In[10]:


wines.dtype


# #### Show top 5 rows 

# In[11]:


wines[:5]


# #### What is the value at 3rd row, 4th column of wine data? 

# In[12]:


print(wines[2,3])


# #### Select first 3 items in 4th column 

# In[13]:


print(wines[:3,3])


# #### Show 1st column 

# In[14]:


wines[:,0]


# #### Show 2nd row 

# In[15]:


wines[1]


# #### Select items from rows 1 to 3 and 5th column 

# In[16]:


print(wines[1:4,4])


# #### Select entire array

# In[17]:


wines[:]


# #### Change 1st value in wines to 100 

# In[18]:


wines[0,0]


# In[19]:


wines[0,0] = 100


# In[20]:


wines[0,0]


# #### Change it back to 7.4 and print
# 

# In[21]:


a = wines[0,0] = 7.4


# In[22]:


a


# ### 1-Dimensional Numpy Arrays

# #### Select 4th row all column values

# In[23]:


a = wines[3,:]


# ####  Display its values

# In[24]:


print(a)


# #### Show the 2 values

# In[25]:


a[1]


# #### int_array = float_array.astype(int)

# In[26]:


a = wines.astype(int)


# In[27]:


a


# ### Vectorization Operations

# #### Increase wine quality score (output variable) by 10 

# In[28]:


wines[:,-1]


# #### increase by 10

# In[29]:


quality = wines[:,-1] + 10


# #### Display update score

# In[30]:


quality


# #### Multiply alcohol of all wine data by 3 times

# In[31]:


alcohol = wines[:,10] * 3


# #### show updated alcohol column

# In[32]:


alcohol


# #### Add quality  column by  itself
# 
# #### wines[:,-1] + wines[:,-1] + 20

# In[33]:


add = quality + quality


# In[34]:


add


# #### Multiply alcohol and wine quality columns. It will perform element wise multiplication 

# In[35]:


multiply = alcohol * quality


# In[36]:


multiply


# ## Broadcasting 
# 

# #### Add every row of wines data with a random array of values 
# 

# In[37]:


import numpy as np


# In[38]:


rand_array = np.random.randn(1,12)

add = rand_array + wines


# #### Show rand_array

# In[39]:


rand_array


# #### add wines and rand_array

# In[40]:


add1 = wines + rand_array
add1

