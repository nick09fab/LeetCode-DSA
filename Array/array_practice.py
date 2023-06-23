import array as arr
#create a general purpose array
my_arr = arr.array('i',[10,20,30,40])

#1. Create an array and traverse
array_elements = [val for val in my_arr]
print(array_elements)

#2. Access individual elements through indexes
array_indexes = [idx for idx in range(0,len(my_arr))]
array_values = [my_arr[idx] for idx in range(0,len(my_arr))]
print(array_indexes)
print(array_values)

#3. Append any value to the array using append() method
value = 2
temp_arr = my_arr.__copy__()
temp_arr.append(value) #append(value) value appends to the last index of the array
print(temp_arr)

#4.Insert value in an array using insert() method
temp_arr = my_arr.__copy__()
temp_arr.insert(1,5) #insert(index,value)
print(temp_arr)

#5. Extend python array using extend() method

"""
extend(iterable):
Append items from iterable to the end of the array. 
If iterable is another array, it must have exactly the same type code; if not, TypeError will be raised.
If iterable is not an array, it must be iterable and its elements must be the right type to be appended to the array.
"""
temp_arr = my_arr.__copy__()
temp_arr.extend([1,2]) #extend(list) -> used to add another list to current list but values will be added at the end of the index
print(temp_arr)

#6. Add items from list into array using fromlist() method
"""
fromlist(list)
Append items from the list. This is equivalent to for x in list: a.append(x) except that if there is a type error, the array is unchanged.
"""
temp_arr = my_arr.__copy__()
temp_arr.fromlist([20,30,50])
print(temp_arr)

#7. Remove any array element using remove() method
temp_arr = my_arr.__copy__()
temp_arr.remove(10) #:remove(value) -> removes the value from the list and move the other elements accordingly
print(temp_arr)

#8. Remove last array element using pop() method
temp_arr = my_arr.__copy__()
temp_arr.pop(len(temp_arr)-1) #:pop(index) -> removes the index value from the list and move the other elements accordingly
print(temp_arr)

#9. Fetch any element through its index using index() method
temp_arr = my_arr.__copy__()
__index__0 = temp_arr.index(10)
__index__1 = temp_arr.index(20)

print(__index__0)
print(__index__1)

#10. Reverse a python array using reverse()
temp_arr = my_arr.__copy__()
temp_arr.reverse()
print(temp_arr)

#11. Get array buffer information through buffer_info() method
"""
Return a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold array’s contents. 
The size of the memory buffer in bytes can be computed as array.buffer_info()[1] * array.itemsize.
This is occasionally useful when working with low-level (and inherently unsafe) I/O interfaces that require memory addresses, 
such as certain ioctl() operations. The returned numbers are valid as long as the array exists and no length-changing operations are applied to it.
"""
temp_arr = my_arr.__copy__()
print(temp_arr.buffer_info()) #buffer_info(mem_address,bytes)

#123. Check for number of occurences of an element using count() method

temp_arr = my_arr.__copy__()

