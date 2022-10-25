class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
#       words = s.split()
#       return(len(words[-1]))
            
        idx = -1
        count = 0
        
        # working on spaces
        while s[idx] == " ": 
            idx -= 1
        # get length of the last element without spaces
        while idx >= -len(s) and s[idx] != " ":
            count += 1
            idx -= 1

        return count
        