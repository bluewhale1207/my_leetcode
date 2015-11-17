# https://leetcode.com/problems/missing-number/

class Solution(object):

    def missingNumber_1(self, nums):
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

    def missingNumber(self, nums):
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

print Solution().missingNumber([])
print Solution().missingNumber([0])
print Solution().missingNumber([0, 1])
print Solution().missingNumber([1, 2])
print Solution().missingNumber([0, 1, 3])
print Solution().missingNumber([0, 2, 3])

print Solution().missingNumber_1([])
print Solution().missingNumber_1([0])
print Solution().missingNumber_1([0, 1])
print Solution().missingNumber_1([1, 2])
print Solution().missingNumber_1([0, 1, 3])
print Solution().missingNumber_1([0, 2, 3])
