"""
- Input: a binary tree [5,4,8,11,null,13,4,7,2,null,null,null,1], and target
- Output: boolean if there's a root-to-leaf sum values equals our target => True, not equal => False

- Solution:
    - Loop through both left and right subtrees and subtract each node value from the target
    - Check if one of the subtrees has path or not

- Complexity:
    - time: O(n)
    - space: O(n)
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        # Check if the current node is a leaf node (no left or right child)
        if root.left is None and root.right is None:
            return targetSum == root.val

        # Return True if either the left or right subtree has a valid path
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
        
        # Return True if either the left or right subtree has a valid path
        return left_sum or right_sum






