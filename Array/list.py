## List Operations

my_list = [1,2,3,4,5]
my_list.insert(2,15)
print(my_list) #not optimal method -> O(n)

my_list.append(2) #O(1)

my_list.extend([1,2,3]) #O(n)

## deleting values from list
"""
- pop()
- delete()
- remove()
"""

my_list.pop() #gets the last element of the list
my_list.pop(2) #removes the value from the list

del my_list[2] #removes the value from the list

my_list.remove(2) #O(n)

