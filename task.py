#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[8]:


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

unique_vals = data['whoAmI'].unique()
one_hot_data = pd.DataFrame(columns = unique_vals)

for val in unique_vals:
    one_hot_data[val] = (data['whoAmI'] == val).astype(int)
    
one_hot_data.head()


# In[ ]:




