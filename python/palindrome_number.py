class Solution(object):
    def isPalindrome(self, x):
        # 效率最高 Runtime: 224 ms
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = 0
        y = x
        while y:
            s = s * 10 + y % 10
            y = y / 10
        return x == s

    def isPalindrome_1(self, x):
        # Runtime: 232 ms
        if x < 0:
            return False
        y = str(x)
        i = 0
        length = len(y)
        while i <= length - 1 - i:
            if y[i] == y[length - 1 - i]:
                i += 1
            else:
                return False
        return True

    def isPalindrome_2(self, x):
        # Runtime: 252 ms
        if x < 0: return False
        return str(x) == str(x)[::-1]


print Solution().isPalindrome(12321)
