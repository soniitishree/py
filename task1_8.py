#Print the sum of the current number and the previous number
##Print the sum of the current number and the previous number
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)