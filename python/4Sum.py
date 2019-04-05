class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums[:-3])):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1

            while j > i and j < len(nums) - 2:

                if j > i + 1 and nums[j - 1] == nums[j]:
                    j += 1
                    continue

                k = j + 1
                l = len(nums) - 1

                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        res.append(
                            sorted([nums[i], nums[j], nums[k], nums[l]]))
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif s > target:
                        l -= 1
                    else:
                        k += 1

                j += 1

        return res



    def fourSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        res = set()
        d = {}
        nums.sort()
        d = defaultdict(list)
        for p in xrange(len(nums)):
            for q in xrange(p + 1, len(nums)):
                d[nums[p] + nums[q]].append([p, q])

        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums) - 2):
                temp = target - nums[i] - nums[j]

                if temp in d:
                    for item in d[temp]:
                        if j < item[0]:
                            res.add((nums[i], nums[j], nums[
                                    item[0]], nums[item[1]]))
        return [list(i) for i in res]
