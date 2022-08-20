class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
    
        return s == '' # if empty then we get valid parenthese
    
    
### STACK METHOD

#         brackets = {'(': ')', '{': '}', '[': ']'}
#         stack = []

#         for char in s:
#             if char in brackets: # if it's the left bracket
#                 stack.append(char)
#             elif not stack or brackets[stack.pop()] != char: # else if it's the right bracket(loop again and remove the left bracket) or the stack is empty

#                 return False

#         return not stack # if stack is empty then we get valid parentheses