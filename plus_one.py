'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

https://leetcode.com/problems/plus-one/
'''

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
