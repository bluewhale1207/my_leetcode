class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str or str in ['+', '-']:
            return 0
        flag = 1
        i = 0
        if str[i] == '-':
            flag = -1
        if str[i] in ['+', '-']:
            i += 1
        sum = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        maxDiv10 = INT_MAX / 10

        while i < len(str) and str[i].isdigit():
            if sum > maxDiv10 or (sum == maxDiv10 and int(str[i]) >= 8):
                return INT_MAX if flag == 1 else INT_MIN
            sum = sum * 10 + int(str[i])
            i += 1
        return sum * flag

print Solution().myAtoi("21474836yyy")
