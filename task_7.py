#https://pynative.com/python-basic-exercise-for-beginners/
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
n = [x for x in range(1,6)]
print(n)

for x in range(1,6):
    for y in range(x):
        print(x,end="")
    print("\n")