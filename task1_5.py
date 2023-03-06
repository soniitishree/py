#https://pynative.com/python-basic-exercise-for-beginners/
#Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
for i, j in zip(list1, list2):
    print(i,j)