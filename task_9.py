#Print the sum of the current number and the previous number
#Create a new list from a two list using the following condition
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result_list=[]
for i in list1:
    if i %2!=0 :
        result_list.append(i)
for i in list2:
    if i %2==0 :
        result_list.append(i)
print(result_list)