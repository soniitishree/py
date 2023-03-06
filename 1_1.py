# Create a string made of the first, middle and last character
str1 = "James"
l = len(str1)-1
m = l//2
print(str1[0],end="")
print(str1[m],end="")
print(str1[l],end="")

# Create a string made of the middle three characters
print("\n------")
print(str1[m-1],end="")
print(str1[m],end="")
print(str1[m+1],end="")

# Append new string in the middle of a given string
print("\n------")
str2="iti"
x= str1[:m]
x += str2 + str1[m:]
print(x)