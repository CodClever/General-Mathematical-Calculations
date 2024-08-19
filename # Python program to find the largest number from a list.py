# Python program to find the in a list

# Creating empty list

list1 = []
 
# Asking number of elements to put in list

num = int(input("Enter number of elements in list: "))
 
# iterating till num to append elements in list

for i in range(1, num + 1):
    ele = int(input("Enter the a number of elements in your list: "))
    list1.append(ele)
     
# Print maximum element

print("Largest number in your list is: ", max(list1))

# For your kind information, this is not written by me, it's copied from other source.
# I am not bad because after making this file, I learnt the code.
