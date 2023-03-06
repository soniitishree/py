#https://pynative.com/python-basic-exercise-for-beginners/
#Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
sqr = [numbers[x] ** 2 for x in range(len(numbers))]
print(sqr)