'''
BMI Calculator: Write a Python program that takes a person's height (in meters)
and weight (in kilograms) as input and calculates their Body Mass Index (BMI).
Print out their BMI and a message indicating whether they are underweight
(<18.5), normal (18.5-24.9), overweight (25-29.9), or obese (>=30).
'''
height = float(input("height in meters: "))
weight = float(input("weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI = ", bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 24.9:
    print("normal weight")
elif 25 <= bmi < 29.9:
    print("overweight")
else:
    print("obese")
