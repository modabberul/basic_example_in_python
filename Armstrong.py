"""
2. Armstrong Number Checker: Write a Python program that takes an integer
input from the user and checks if it is an Armstrong number (a number that is
equal to the sum of its own digits raised to the power of the number of digits)
using a for loop.

"""
num = int(input())
num1 =num
num2 = num
cout =0
while num !=0:
    cout +=1
    num = num // 10
    
#ekhon count == digit

#temp = cout
sum = 0
while num1 != 0:
    digit = num1 % 10
    sum += digit**cout
    num1 = num1 // 10
    
if sum == num2:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")