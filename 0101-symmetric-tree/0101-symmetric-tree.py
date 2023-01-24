# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        else:
            return self.is_mirror(root.left, root.right)
        
        
    def is_mirror(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val == right.val:
            # check the outer part of tree
            outer_part = self.is_mirror(left.left, right.right)

            # check the inner part of tree
            inner_part = self.is_mirror(left.right, right.left)

            return outer_part and inner_part

        else:
            return False
