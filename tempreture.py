'''
Temperature Converter: Write a Python program that takes a temperature input
in Celsius and converts it to Fahrenheit if the temperature is above 0°C, or to
Kelvin if the temperature is below 0°C.
'''
C = float(input("temperature in Celsius: "))

if C > 0:
    F = (C * 9/5) + 32
    print("The temperature in Fahrenheit is:", F,"F")
elif C < 0:
    K = C + 273.15
    print("The temperature in Kelvin is:",K, "K")
else:
    print("freezing point of water.")
