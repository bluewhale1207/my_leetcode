
"""
https://leetcode.com/submissions/detail/46278408
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        # Runtime: 56 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums)) * 2 - sum(nums) 

    def singleNumber_1(self, nums):
        # Runtime: 52 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        import operator
        return reduce(operator.xor, nums)
        
