#Print the sum of the current number and the previous number
#reverse Number
num = int(input("enter num: \n"))
or_num = num
rev = 0
while num > 0:
    r = num % 10
    rev = rev *10 + r
    num = num // 10


print(rev,"is reverse of",or_num)
