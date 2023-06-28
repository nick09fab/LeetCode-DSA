class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        n = len(needle)
        idx = []
        for r in range(len(haystack)):
            if n <= len(haystack) and haystack[r:n] == needle:
                idx.append(r)
            else:
                n += 1

        return min(idx) if idx else -1





haystack = "butsad"
needle = "sad"

print(Solution().strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"

print(Solution().strStr(haystack, needle))
