"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

"""
import unittest
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        sign = 'pos' if x > 0 else 'neg'
        if sign == 'neg':
            x = x * -1
        while x > 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x //= 10

        if sign == 'neg':
            rev = rev * (-1)
        return rev


#Test Case 1
x = Solution()
num = 210
try:
    assert (x.reverse(num) == 12)
except AssertionError:
    print(f'The case failed for {num}')
#Test Case 2
num = 123
try:
    assert (x.reverse(num) == 210)
except AssertionError:
    print(f'The case failed for {num}')