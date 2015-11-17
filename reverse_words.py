class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([item.strip() for item in reversed(s.split())])
        
        
    def reverseWords_1(self, s)
        return ' '.join(reversed(s.split()))


print Solution().reverseWords('')
print Solution().reverseWords('   ')
print Solution().reverseWords(' b  a  ')
