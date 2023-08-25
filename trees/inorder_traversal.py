# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
            if curr.right:
                stack.append(root.right)
            if curr.left:
                stack.append(root.left)
        return res
