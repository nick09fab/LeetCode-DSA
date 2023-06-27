class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = min(strs, key=len)
        res = ""
        for i in range(len(n)):
            for char in strs:
                if char[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return n






strs = ['flower','flow','flight']

print(Solution().longestCommonPrefix(strs))