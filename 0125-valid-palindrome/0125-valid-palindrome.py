"""
- Input: a phrase e.g. "A man, a plan, a canal: Panama"
- Output: boolean if the input phrase reads the same forward and backward

- Solution: 
    - Cleaning phrase from:
        - uppercase to lowercase
        - remove any special characters (non-alphanumeric characters)
        - remove any spaces between characters

    - Create new variable to store the new phrase read from end to beginning
    - Compare the orignal phrase (after cleaning) to the new phrase

- Complexity:
    - time: O(n)
    - space: O(n)
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove any non-alphanumeric characters, spaces, and lowercase
        new_s = s.lower().replace(' ', '')
        new_s = re.sub(r'[^a-zA-Z0-9]', '', new_s)

        # Read the phrase from end to beginning
        verced_s = new_s[::-1]

        return verced_s == new_s









