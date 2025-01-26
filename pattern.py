'''
5. Print the pattern (for/while):
1
22
333
4444
55555

'''
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()