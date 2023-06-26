# Calcualte the sum of 2D diagnols
"""
Given the 2D list calculate the sum of diagonal elements

mylist2D = [[1,2,3],[4,5,6],[7,8,9]] #15
"""
# def diagnol_sum(matrix):
#     all_values  = []
#     for idx,lst in enumerate(matrix):
#         value = lst[value]
#         all_values.append(value)
#     return  all_values

# Primary Diagonal and Secondary Diagonal

mylist2D = mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        res = 0  # secondary col

        for row in range(n):
            # primary_diagnol
            res += mat[row][row]

            # secondary matrix
            res += mat[row][(row * -1) - 1]
        if n & 1:
            # avoid adding center number twice
            res -= mat[n // 2][n // 2]
        return res

print(Solution().diagonalSum(mylist2D))
