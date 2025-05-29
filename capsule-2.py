# CAPSULE 2 DO IT YOURSELF

# q1: Write a program that prompts the user to input a year, checks 
# whether it's a leap year or not, and then prints the result.

print("\nQUESTION 1\n")

def func(n):
  if n%4==0:
    if n%100==0:
      return n%400==0
    return True
  return False

year = int(input("Enter year: "))

if (func(year)):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

# q2: Write a Python program that prompts the user to input a word. 
# The program should then determine and output the count of vowels 
# (a, e, i, o, u) in the provided word. Additionally, consider that 
# the word can be in either uppercase or lowercase.

print("\nQUESTION 2\n")

def func(word):
  count=0
  vowels=['a','e','i','o','u']
  for i in word:
    if i in vowels:
      count+=1
  return count

word = input("Enter a word: ")

count=func(word)

if (count):
  print(f"There are {count} vowels in {word}")
else:
  print(f"There are no vowels in {word}")

# q3: Write a Python program that allows the user to input a list 
# of 6 names. After receiving the list, the program should print 
# only the names that start with the letter 'a', regardless of 
# whether the letter is uppercase or lowercase.

print("\nQUESTION 3\n")

def func(list1):
  for i in list1:
    if i.lower().startswith('a'):
      print(i)

list1=[]
num=6

while num!=0:
  s=input("Enter name: ")
  list1.append(s)
  num-=1

print("Names that start with 'a': ")
func(list1)

# q4: Write a Python program that takes a list of 10 integers as input. 
# Your program should iterate through the list and print the following:
# For each even number encountered, print the number squared.
# For each odd number encountered, print the number cubed.

print("\nQUESTION 4\n")

def func(l):
    for i in l:
        if i%2==0:
            print(f"{i*i} ")
        else:
            print(f"{i*i*i} ")

while True:
    numbers = input("Enter 10 numbers separated by space: ").split()
    if len(numbers) == 10:
        numbers = list(map(int, numbers))
        func(numbers)
        break
    else:
        print("Please enter exactly 10 numbers.")

# q5: Imagine you're ordering flowers from a local delivery service. 
# They offer a selection of beautiful flowers, including roses. 
# Each rose is priced at Rs. 10. Along with your choice of roses, 
# you'll need to provide the count of roses you wish to order and 
# the delivery distance. The delivery charges are as follows: 
# Rs. 25 for distances within 5 kilometers, Rs. 50 for distances 
# between 5 and 10 kilometers, and Rs. 75 for distances greater than 
# 10 kilometers. Write a Python program that prompts the user to enter 
# the count of roses and the delivery distance, then calculates and 
# displays the total price to pay, including both the cost of roses 
# and the delivery charge.

print("\nQUESTION 5\n")

def func(n):
  if(n<5):
    return 25
  if (n<10):
    return 50
  return 75

count = int(input("Enter count of roses: "))
dist= int(input("Enter distance(in km): "))

print(f"Total cost: {(count*10)+func(dist)}")

