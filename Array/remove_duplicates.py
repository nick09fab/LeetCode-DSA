class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1 #right pointer
        for r in range(1,len(nums)): #i -> left pointer
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l


nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))