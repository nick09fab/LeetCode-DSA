class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            if target in nums:
                if nums[i] == target:
                    return i
            else:
                if i < n-1 and nums[i] < target < nums[i+1]:
                    return i + 1
        return n if target > max(nums) else 0



#Test Case 1
nums = [1,3,5,6]
target = 5
print(Solution().searchInsert(nums, target))

#Test Case 2
nums = [1,3,5,6]
target = 2
print(Solution().searchInsert(nums, target))

#Test Case 3
nums = [1,3,5,6]
target = 7
print(Solution().searchInsert(nums, target))

#Test Case 4
target = 0
print(Solution().searchInsert(nums, target))
