import numpy as np

#day1 - 11,15,16,29
#day2 - 22,11,12,90
#day3 - 32,17,39,70

twoDarray = np.array([[11,15,16,29],
                      [22,11,12,90],
                      [32,17,39,70],
                      [12,3,4,7]
                    ])
print(twoDarray) #space complexity O(mn) m rows and n columns

# Insert into 2D Array
new_twodarr_row = np.insert(twoDarray, 3, [[1,2,3,5]],axis=0 ) #np.insert(array, position, elements, row/column axis) 1=col 0 = row
print(new_twodarr_row)
new_twodcol = np.insert(twoDarray, 0, [[1,2,3,5]],axis=1 ) #np.insert(array, position, elements, row/column axis) 1=col 0 = row
print(new_twodcol)
#Append 2D array
twoDarray = np.array([[11,15,16,29],
                      [22,11,12,90],
                      [32,17,39,70],
                      [12,3,4,7]
                    ])
_twoDarray = np.append(twoDarray,[[1,2,3,4]],axis=0) #[1,2,4] -> 1-Dimension Array
print(_twoDarray)

import random

lst = ['fruit','apple','carrot']
random.shuffle(lst)
print(lst)