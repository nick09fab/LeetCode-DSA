class Solution(object):
    def missing_number(self,arr,n):

        """
        array is in 1 to n
        n = 10
        total = 10 * 11/2 = 55
        sum_array = 50
        missing = 55 -50 = 5
        """

        # Using arithmetic progression to get the missing value
        total = n * (n+1) // 2 #total of values given
        _sum = sum(arr) #sum of the array
        missing_value  = total - _sum

        return missing_value


lst = [1,2,3,4,6]
num = 6
print(Solution().missing_number(lst,num)
)

lst = [5,10,20]
num = 10
print(Solution().missing_number(lst,num)
)
# print(Solution().missing_number((,10)))