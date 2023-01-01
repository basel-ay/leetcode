class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # A string is called a palindrome string if the reverse of that string is the same as the original string.
        res = ""
        for i in range(len(s)):
            # odd case, like "aba" get_the_longest_palindrome(s, i, i)
            # even case, like "abba" get_the_longest_palindrome(s, i, i+1)
            res = max(self.get_palindrome(s, i, i), self.get_palindrome(s, i, i+1), res, key=len) # longest palindrome by len

        return res
    
    def get_palindrome(self, s, l, r):
            '''
            Get the palindrome, (l, r) are the middle indexes from inner to outer
            print(get_palindrome(s, 1, 1)) => 'bab' for s = 'babad'
            '''
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]
        