# Create arrays using two python modules
"""
1.Arrays need to be declared. Lists don't, since they are built into Python.
In the examples above, you saw that lists are created by simply enclosing a sequence of elements into square brackets.
Creating an array, on the other hand, requires a specific function from either the array module
(i.e., array.array()) or NumPy package (i.e., numpy.array()). Because of this, lists are used more often than arrays.

2.Arrays can store data very compactly and are more efficient for storing large amounts of data.

3.Arrays are great for numerical operations; lists cannot directly handle math operations.
For example, you can divide each element of an array by the same number with just one line of code.
 If you try the same with a list, you'll get an error.

--- Use Cases
1. If you need to store a relatively short sequence of items and you don't plan to do any mathematical operations with it,
 a list is the preferred choice. This data structure will allow you to store an ordered, mutable, and indexed sequence
 of items without importing any additional modules or packages.

2.If you have a very long sequence of items, consider using an array. This structure offers more efficient data storage.

3. If you plan to do any numerical operations with your combination of items, use an array.
Data analytics and data science rely heavily on (mostly NumPy) arrays.
"""

"""
Creating an array using array python module
"""
import array as arr

my_array = arr.array('i') #O(1)
my_array = arr.array('f',[1,2,3,4,5]) #O(n)

"""
inserting into an array
"""
my_array = arr.array('i',[1,2,4,5,7])
# my_array.insert(0, 10) #worst case time complexity O(n) -> rotating other elements
my_array.insert(len(my_array),10) #space complexity O(1) -> only adds an element to one index and doesnt move other elements

"""
Linear Search
"""
def linearSearch(A,element):
    for i in range(0,len(A)):
        if A[i] == element:
            return i
    return None

# print(linearSearch([1,2,3,4,5],5)
# )

"""
Delete/Remove Element
"""
my_array = arr.array('i', [1,2,4,5,6])
my_array.remove(6) #remove the element -> O(n) Worst Case elements needs to be re-ordered
print(my_array)


#
#
# import numpy as np
#
# np_array = np.array([], dtype=int) #O(1)
# print(np_array)
# np_array = np.array([1,2,4,6], dtype=float) #O(n)
# print(np_array/3)
#

