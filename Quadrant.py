'''
Quadrant Identifier: Write a Python program that takes the coordinates (x, y) of
a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or 4th).
'''
x = int(input())
y = int(input())
if(x==0):
    print("Y Axis")
elif(y==0):
    print("X Axis")
elif(x<0 and y>0):
    print("2nd")
elif(x>0 and y>0):
    print("1st")
elif(x>0 and y<0): 
    print("4th")
elif(x<0 and y<0):
    print("3rd")