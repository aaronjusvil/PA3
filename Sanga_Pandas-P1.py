#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd #allows the use of the pandas library and its functions by calling on it using pd.


# Problem 1

# In[15]:


cars = pd.read_csv('cars.csv')
#Calls on the dataframe saved on .csv file saved on the folder, and assigns it to "cars"

first_last_5 = pd.concat([cars.head(), cars.tail()])
#Gets the first and last 5 rows and puts them together into one new dataframe, which is assigned to variable 'first_last_5'

display('Original Dataframe:', cars)
#Displays the original dataframe before it was sliced.

print('\n')

display('First and Last 5 Rows: ', first_last_5)
#Displays the sliced dataframe which shows the first and last 5 rows of the original dataframe


# In[ ]:




