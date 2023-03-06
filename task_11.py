#Print the sum of the current number and the previous number
#Calculate income tax
sal = int(input("enter salary: \n"))
per = 0
tax = 0
s = ""
if sal <= 10000:
    tax = 0
    s = "10000 x 0% ="
elif sal > 10000 and sal <= 20000:
    tax = (sal-10000) * 0.1
    print(tax)
    s = "10000 x 0% + 10000 x 10% ="
else:
    tax = (10000) * 0.1 + (sal-20000) * 0.2
    print(tax)
    s = "10000 x 0% + 10000 x 10% + " + str(sal - 20000) + "x 20% =" 


print(s,tax)
