class Solution(object):


    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        closest = nums[0] + nums[1] + nums[2] - target
        res = nums[0] + nums[1] + nums[2]
        for i in range(length - 2):
            j, k = i + 1, length - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k] - target
                if abs(closest) > abs(s):
                    closest = s
                    res = nums[i] + nums[j] + nums[k]

                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    return target
        return res
