class Solution(object):

    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums) - 1
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length

            while j < k:
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                while j < k and nums[i] + nums[j] + nums[k] < 0:
                    j += 1

                if j < k and nums[i] + nums[j] + nums[k] == 0:
                    if (k < len(nums) - 1 and nums[k] != nums[k + 1]) \
                            or (j - 1 < i and nums[j] != nums[j - 1]):
                        res.append(sorted([nums[i], nums[j], nums[k]]))
                    elif k == len(nums) - 1 or j - 1 == i:
                        res.append(sorted([nums[i], nums[j], nums[k]]))
                    k -= 1
                    j += 1
        return res
