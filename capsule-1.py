# q1: Write a Python program that takes user input for their name and greets the user. 
# Then, prompt the user to enter two values. After receiving the values, swap them and 
# print both the ordiginal values and the swapped values.

print("QUESTION 1\n")
name = input("Please enter your name: ")
print(f"Welcome, {name}!\n")

num1=input("Enter value 1: ")
num2= input("Enter value 2: ")

print(f"Old value of num1: {num1}\nOld value of num2: {num2}\n")

num1,num2=num2,num1

print(f"New value of num1: {num1}\nNew value of num2: {num2}\n")

# q2: Write a Python program that asks the user to input the radius of a circle. 
# Calculate the area of the circle using the formula area = π * radius^2, 
# where π (pi) is a constant approximately equal to 3.14. Print out the calculated area. 
# Ensure that the user input for the radius is converted to a float data type before 
# performing calculations.

print("QUESTION 2\n")

rad = float(input("Enter radius: "))
pi=3.14
area=pi* rad**2
print(f"Area of circle with given radius is: {area}\n")

# q3: Write a Python program where the user is prompted to input their birth year. 
# The program should then calculate and display the user's current age.

print("QUESTION 3\n")

year=int(input("Please enter birth year: "))
print(f"Your current age in 2025 is: {2025-year}\n")

# q4: Imagine you're a bakery owner and you want to personalize messages for your customers. 
# Write a Python program where customers are prompted to input their name and favorite cake flavor. 
# The program should then print a customized message saying: "Hello, [name]! We're delighted to 
# serve you your favorite [favorite_cake] cake on your birthday. Happy Birthday."

print("QUESTION 4\n")

name=input("Enter your name: ")
cake=input("Enter your favourite cake flavour: ")

print(f"Hello, {name}! We're delighted to serve you your favorite {cake} cake on your birthday. Happy Birthday.\n")

# q5: Write a Python program to calculate the simple interest with user input for principal amount, rate, and time.

print("QUESTION 5\n")

amt=float(input("Enter principal amount: "))
rate=float(input("Enter rate: "))
time=float(input("Enter time: "))

si=(amt*rate*time)/100

print(f"The simple interest will be: {si}")