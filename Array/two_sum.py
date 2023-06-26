"""
Follow Up question
- Does array have only +ve or -ve nums?
- Same pair repeat twice, should we print both?
- reverse of pair is acceptable eg. (4,1) or (1,4)
- Only distinct pairs? (3,3)
- big is the array?
"""
# O(m*n) -> O(n^2) m
# def two_sum(arr, num):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j] == num:
#                 return [i,j]
#
#
# print(two_sum([2,7,11,15], 9))
#
# print(two_sum([3,2,4], 6))
#
# print(two_sum([3,3], 6))


#O(n) solution
# One pass hash table
def two_sum(nums, target):
    seen = {}
    #[3,2,4]
    for i,num in enumerate(nums):
        complementary = target - num

        if complementary in seen:
            return [seen[complementary],i]

        #add it to the dictionary
        seen[num] = i


print(two_sum([3,2,4],6))