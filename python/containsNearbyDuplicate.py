class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # 56ms
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        
        for i, item in enumerate(nums):
            if item in d and i - d[item] <= k:
                return True
            else:
                d[item] = i
        return False
