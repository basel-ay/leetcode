class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        string_x = str(x)
        return string_x == string_x[::-1]