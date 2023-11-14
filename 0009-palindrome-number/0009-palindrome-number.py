"""

The number equally read Right, left and vice versa
    - Convert the integer to string.
    - Create an empty list to store the vice versa number (from Right).
    - If the vice versa list equal to the main one.

Big O(n) for time and space complexity
   - The function has to iterate over the entire string to reverse it, and then iterate over the entire string again to compare it to the original string. This means that the time complexity is linear in the length of the string, O(n).
   
"""


class Solution(object):
    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
        
    #     string_x = str(x)
    #     return string_x == string_x[::-1]

        def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            string_x = str(x)
            versed_list = string_x[::-1] # read from the end

            return True if versed_list==string_x else False
            