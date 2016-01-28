class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        flag = 1
        for item in range(len(digits)-1, -1, -1):
            num = digits[item] + flag
            res.append(num % 10)
            flag = num / 10
        if flag == 1:
            res.append(1)
        return res[::-1]
