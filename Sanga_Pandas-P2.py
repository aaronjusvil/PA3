#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #allows the use of the pandas library and its functions by calling on it using pd.


# Problem 2

# In[4]:


cars = pd.read_csv('cars.csv')
#Calls on the dataframe saved on .csv file saved on the folder, and assigns it to "cars"

part_a = cars.loc[0:4, ['Model', 'mpg', 'cyl', 'hp', 'wt', 'vs', 'gear']]
#Looks for and obtains the "cars" dataframe's rows from index 0-4, including 4, and displays their models, and then the odd numbered columns that come after,
#which are the 'mpg', 'cyl', 'hp', 'wt', 'vs', and 'gear' columns, and stores it to variable 'part_a'

part_b = cars.iloc[[0]]
#looks for and gets the row with index zero, which is the row of the model 'Mazda RX4', which is stored in variable 'part_b'

part_c = cars.loc[[23], ['Model', 'cyl']]
#looks for and gets the row with index 23, which is the row of 'Camaro Z28', and displays its model and its 'cyl' columns, which is stored in variable 'part_c'

part_d = cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
#Looks for and gets the rows of ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’, and displays its model, 'cyl', and 'gear' columns, which is stored in variable 'part_d'

#These codes display each of the dataframes along with their labels, staring from the original dataframe to the last, which is 'part_d'
display('Original Dataframe:', cars)

print('\n')

display('Part a. ', part_a)

print('\n')

display('Part b. ', part_b)

print('\n')

display('Part c. ', part_c)

print('\n')

display('Part d. ', part_d)


# In[ ]:




