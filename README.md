Aaron Justine V. Sanga 2ECE-A
# PA3 - Python Data Analysis

In this programming assignment, we are asked to apply and use the different codes and functions in the Pandas library, in different situations.

```import pandas as np``` is used all throughout this assignment, to be able to call the Pandas library and use its functions by using pd

***Problem 1:*** Load a .csv file into a dataframe, and display its first and last 5 rows.
```
cars = pd.read_csv('cars.csv')
#Calls on the dataframe saved on .csv file saved on the folder, and assigns it to "cars"

first_last_5 = pd.concat([cars.head(), cars.tail()])
#Gets the first and last 5 rows and puts them together into one new dataframe, which is assigned to variable 'first_last_5'

display('Original Dataframe:', cars)
#Displays the original dataframe before it was sliced.

print('\n')

display('First and Last 5 Rows: ', first_last_5)
#Displays the sliced dataframe which shows the first and last 5 rows of the original dataframe
```

***Code Description:*** This code calls on a .csv file dataframe using ```pd.read_csv('cars.csv')``` and saves it into ```cars```. ```cars.head()``` and ```cars.tail()``` call on the first and last five rows of the dataframe automatically. These two are concatenated and connected to eachother, creating a single new dataframe with only the needed rows, and that new dataframe is saved into variable ```first_last_5```. The two dataframes are presented using ```display()```, along with their labels. The output shows:

<img width="469" height="835" alt="image" src="https://github.com/user-attachments/assets/6335f766-56f3-4848-94c4-795a2c2c966c" />                      <img width="491" height="303" alt="image" src="https://github.com/user-attachments/assets/eb8028fc-efb4-4283-a452-9fe9b9d6cf20" />




***Problem 2:*** Using the dataframe ```cars``` in problem 1, extract the following information using subsetting, slicing and indexing operations.

***a.)*** Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
```
cars = pd.read_csv('cars.csv')
#Calls on the dataframe saved on .csv file saved on the folder, and assigns it to "cars"

part_a = cars.loc[0:4, ['Model', 'mpg', 'cyl', 'hp', 'wt', 'vs', 'gear']]
#Looks for and obtains the "cars" dataframe's rows from index 0-4, including 4, and displays their models, and then the odd numbered columns that come after,
#which are the 'mpg', 'cyl', 'hp', 'wt', 'vs', and 'gear' columns, and stores it to variable 'part_a'
```
***Code Description:*** ```cars.loc[0:4, ['Model', 'mpg', 'cyl', 'hp', 'wt', 'vs', 'gear']]``` finds and gets the rows of index 0-4, but only getting the columns labeled 'Model', 'mpg', 'cyl', 'hp', 'wt', 'vs', 'gear', which are the odd numbered columns of the original dataframe. This new dataframe is saved into variable 'part_a'.

***b.)*** Display the row that contains the ‘Model’ of ‘Mazda RX4’.
```
part_b = cars.iloc[[0]]
#looks for and gets the row with index zero, which is the row of the model 'Mazda RX4', which is stored in variable 'part_b'
```
***Code Description:*** This line of code locates the row with index 0, and displays that whole row, which is the row of 'Mazda RX4', and saves it in the variable 'part_b'.

***c.)*** How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? 
```
part_c = cars.loc[[23], ['Model', 'cyl']]
#looks for and gets the row with index 23, which is the row of 'Camaro Z28', and displays its model and its 'cyl' columns, which is stored in variable 'part_c'
```
***Code Description:*** looks for and gets the row with index 23, which is the row of 'Camaro Z28', and displays its model and its 'cyl' columns, which is stored in variable 'part_c'.

***d.)*** Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

```
part_d = cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
#Looks for and gets the rows of ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’, and displays its model, 'cyl', and 'gear' columns, which is stored in variable 'part_d'.
```
***Code Description:*** Looks for and gets the rows of ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’, and displays its model, 'cyl', and 'gear' columns, which is stored in variable 'part_d'.

Overall Code:
```
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
```
The 5 dataframes are displayed, including the orignal dataframe, along with their labels, by using the ```display()``` function. The output is as shown:

<img width="473" height="833" alt="image" src="https://github.com/user-attachments/assets/39f0e3a0-86be-4a85-886f-1e9db1b12f64" />          <img width="462" height="511" alt="image" src="https://github.com/user-attachments/assets/1ec8f052-7f6d-4d29-a2ce-16be74cfb733" />






