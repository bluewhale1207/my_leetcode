class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i, item in enumerate(nums):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                return True
        return False
        
    def containsDuplicate_1(self, nums):
         return len(set(nums)) < len(nums)
         
    
    def containsDuplicate_2(self, nums):
         s = set()
         for item in nums:
             if item in s:
                 return True
              else:
                  s.add(item)
          return False
