"""
Largest among Three Numbers: Write a Python program that takes three
numbers as input and prints out the largest among them. 

"""
print("Enter three numbers:")
num1 = int(input())
num2 = int(input())
num3 = int(input())

la_num = num1

if num2 > la_num:
    la_num = num2

if num3 > la_num:
    la_num = num3

print("Largest number:", la_num)
