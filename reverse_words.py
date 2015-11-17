class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([item.strip() for item in reversed(s.split())])


print Solution().reverseWords('')
print Solution().reverseWords('   ')
print Solution().reverseWords(' b  a  ')
