"""
- Input: binary tree => [3,9,20,null,null,15,7]
- Output: boolean: True => balanced BT, False => unbalanced BT

- What is balanced binary tree?:
    - balanced binary tree is a binary tree in which the depth of the two subtrees of every node
      never differs by more than one.

- Loop through left and right subtrees using recursion untill end, then check our conditions of the BBT

- Complexity:
    - :time: O(n log n) for balanced tree, and for unbalanced tree O(n**2)
    - :space: O(log n) for balanced trees and O(n) in the worst case for unbalanced trees.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) != -1

    def height(self, root):
        if root is None:
            return 0

        # Recursive case: Calculate the height of left and right subtrees
        left_height, right_height = self.height(root.left), self.height(root.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        
        # Return the maximum height between left and right subtrees + 1 for the current node
        return max(left_height, right_height) + 1
