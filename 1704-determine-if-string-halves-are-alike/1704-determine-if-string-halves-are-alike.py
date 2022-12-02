class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = b = 0
        i, j = 0, len(s)-1 # split given stirng into two halves

        while i < j:
            # check if the char is vowels then add it
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1
            j -= 1
        
        return a==b # check if the two halves have the same number of vowels