"""
- Inputs: array of numbers eg. [1,2,3,1]
- Outputs: boolean, true if contains duplicates and false if not

- Solution:
    - Create a set to to keep track of unique elements
    - Loop through the array and check if a number already in our set that means the array contains duplicates
    
- Comlexity:
    - time: O(n):
        - We iterate through the array once using a loop, which takes O(n) time.
    
    - space: O(n):
        - The set() "seen" stores unique elements from the array. In the worst case, where all elements are distinct, the set will contain n unique elements, leading to O(n) space usage.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Use a set to keep track of unique elements
        seen = set()

        # Loop through the numbers in the array
        for num in nums:
            # Check if the number in already in our set
            if num in seen:
                return True
            
            # Otherwise, add the number to the set
            seen.add(num)

        # If the loop completes without finding any duplicates, return False
        return False









