class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs)==0: 
            return ""
        
        prefix = strs[0] #first item
        
        for item in strs:
            while not item.startswith(prefix):
                prefix = prefix[:-1]
                
        return prefix                
        
        