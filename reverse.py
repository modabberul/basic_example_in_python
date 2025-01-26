'''3. Number Reverser: Write a Python program that takes an integer input from the
user and prints its reverse using a while loop.
'''
num = int(input())
rev = 0
while num != 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10

print("reversed number is:", rev)