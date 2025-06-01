# q1: Write a Python program to initialize a 3x3 NumPy array with any integer values of your choice. 
# Then, perform the following operations:
# Multiply the entire array by 2.
# Add 5 to each element of the array.
# Calculate the square of each element in the array.
# Print the original array and the results of each operation.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('\nQUESTION 1\n')
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original array: ")
print(arr)
res1=arr*2
print("Array after multiplication by 2: ")
print(res1)
res2=arr+5
print("Array after addition of 5 to each element: ")
print(res2)
res3=pow(arr,2)
print("Array after squaring each element: ")
print(res3)

# q2: Write a Python program to initialize a 3x3 NumPy array with any integer values of your choice. 
# Then, perform the following slicing operations:
# Extract the first row of the array.
# Extract the last column of the array.
# Extract a 2x2 sub-array from the center of the original array.

print('\nQUESTION 2\n')
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original array: ")
print(arr)
print(f"First row of array is {arr[0,:]}");
print(f"Last column of array is {arr[:,2]}")
print(f"A 2x2 sub-array from the center of original array is \n{arr[0:2, 1:3]}")

# q3: Write a program to create a DataFrame in Python to store the names 
# and marks of 10 students. Each row of the DataFrame should represent a 
# student, with columns as 'Name' and 'Marks'. Populate the DataFrame 
# with appropriate data and then print it.

print('\nQUESTION 3\n')
data={
  'Names': [
    "Aarav", "Ishita", "Rohan", "Meera", "Kabir",
    "Anaya", "Vihaan", "Tara", "Dev", "Saanvi"
],
'Marks':[85, 92, 78, 88, 90, 76, 83, 95, 67, 89]
}
df=pd.DataFrame(data)
print(df)

# q4: Write a python program to create a DataFrame representing the 
# names and income of 5 employees. The DataFrame should include columns 
# ' Employee_name’ and ‘Income', and each row should correspond to an 
# individual employee. Use the indices 'a', 'b', 'c', 'd', and 'e' for 
# the DataFrame entries to uniquely identify each employee.

print('\nQUESTION 4\n')
data={
  'Employee_name':[
    "Aarav", "Ishita", "Rohan", "Meera", "Kabir"],
    'Income':[10000,250000,45000,5000,23000]
}
df=pd.DataFrame(data,index=['a','b','c','d','e'])
print(df)

# q5: Imagine you're tasked with visualizing data using Python. 
# You have the following dataset representing the frequency of 
# occurrences for categories A, B, C, D, and E, stored in two lists:
# x = ['A', 'B', 'C', 'D', 'E']
# y = [10, 20, 15, 25, 30]
# Write a Python script that creates a bar plot to visualize this data. 
# The categories A, B, C, D, and E should be displayed on the x-axis, 
# while the corresponding frequencies should be displayed on the y-axis.

print('\nQUESTION 5\n')
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]
bar_graph=plt.bar(x,y)
plt.xlabel('Categories')
plt.ylabel('Frequencies')
plt.show()
