
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_csv('/Users/garimajain/Desktop/data_viz_1.csv')


# In[3]:

df1 = df.set_index("METHOD OF LEAK")


# In[4]:

df2 = df1.loc[:, "Entity": "NO OF RECORDS STOLEN"]


# In[ ]:



