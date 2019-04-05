class Solution(object):
  # https://leetcode.com/problems/move-zeroes/
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for item in range(len(nums)):
            if nums[item]:
                nums[item], nums[pos] = nums[pos], nums[item]
                pos += 1
        return nums

    def moveZeroes_1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        nums[k:] = [0] * (len(nums) - k)
        return nums
