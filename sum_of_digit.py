'''
Sum of Digits: Write a Python program that takes an integer input from the user
and calculates the sum of its digits using a while loop.
'''
num = int(input())
sum_of_digits = 0
while num != 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

print("Sum=",sum_of_digits)
