#Print the sum of the current number and the previous number
#Check Palindrome Number
num = int(input("enter num: \n"))
or_num = num
rev = 0
while num > 0:
    r = num % 10
    rev = rev *10 + r
    num = num // 10

if or_num == rev:
    print("{0} is palindrome",or_num)
else:
    print("{0} is not palindrome",or_num)