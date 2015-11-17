# https://leetcode.com/problems/missing-number/
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
'''
class Solution(object):
    def missingNumber(self, nums):
        # Runtime: 56 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        length = len(nums)
        sum_1 = (length + 1) * length / 2
        sum_2 = sum(nums)
        return sum_1 - sum_2

    def missingNumber_1(self, nums):
        # Runtime: 76 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        nums.sort()
        end = nums[-1]
        sum_1 = (end + 1) * end / 2
        sum_2 = sum(nums[:end + 1])
        if sum_2 == sum_1:
            if 0 not in nums:
                return 0
            else:
                return end + 1
        return sum_1 - sum_2

    def missingNumber_2(self, nums):
       # Runtime: 104 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        nums.sort()
        a = list(set(range(len(nums))) ^ set(nums))
        return a[0] if a else nums[-1] + 1


print Solution().missingNumber([])
print Solution().missingNumber([0])
print Solution().missingNumber([0, 1])
print Solution().missingNumber([1, 2])
print Solution().missingNumber([0, 1, 3])
print Solution().missingNumber([0, 2, 3])
