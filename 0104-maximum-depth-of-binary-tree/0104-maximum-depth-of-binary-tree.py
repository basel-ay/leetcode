# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Check if the tree is empty
        if root is None:
            return 0
        
        # Compute each subtree depth
        else:
            l_depth = self.maxDepth(root.left)
            r_depth = self.maxDepth(root.right)
            
            # Use the larger one
            # Get the max of max depths of left and right subtrees and add 1 to it for the current node
            if l_depth > r_depth:
                return l_depth + 1
            
            else:
                return r_depth + 1
