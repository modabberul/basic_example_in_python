'''
Age Classifier: Write a Python program that takes a person's age as input and
prints out whether they are an infant (0-1), toddler (1-3), child (4-12), teenager
(13-19), adult (20+).
'''
age = int(input())
if(age==0 or age==1):
    print("infant")
elif(age>=1 and age<=3):
    print("toddler")
elif(age>=4 and age<=12):
    print("child")
elif(age>=13 and age<=19):
    print("teenager")
elif(age>=20):
    print("adult")
