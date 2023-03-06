#Print the sum of the current number and the previous number
#https://pynative.com/python-basic-exercise-for-beginners/
l = [x+(x-1) if x != 0 else 0 for x in range(10)]
print(l)