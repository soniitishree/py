#Print multiplication table form 1 to 10
#https://pynative.com/python-basic-exercise-for-beginners/
for x in range(1,11):
    for y in range (x,x*11,x):
        print(y,end=" ")
    print("\n")