"""
- Convert array of nums to BST which following the below rules:
    - left child < parent node
    - right child > parent node

- Balanced BST:
    - The depth of the two subtrees of every node never differs by more than one.

- As it's a SORTED array, so we can get the middle element to be our root, then assign all left elements to the left, and all right elements of the root to the right using RECURSION.

Time and Space complexity:
    :time: O(n)
    :space: O(log n)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Check if the array is empty
        if len(nums) == 0:
            return None
        
        # Set the middle number in the array 
        mid_element = len(nums) // 2
        
        # Initialize our tree with the mid number as root
        root = TreeNode(nums[mid_element])

        # Assign the lesser elements of the mid to the left subtree
        root.left = self.sortedArrayToBST(nums[:mid_element])

        # Assign the bigger elements of the mid to the right subtree
        # Use mid_element+1 to avoid duplicating the middle element 
        root.right = self.sortedArrayToBST(nums[mid_element+1:])

        return root
