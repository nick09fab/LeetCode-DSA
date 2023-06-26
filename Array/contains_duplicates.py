class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False





#Test case 1
nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))
#Test case 2
nums = [1,2,3,4]
print(Solution().containsDuplicate(nums))
#test case 3
nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))