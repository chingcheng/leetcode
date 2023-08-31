# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current = root
        stack = []
        result = []
        while current or stack:
            if current is not None:
                result.append(current.val)
                stack.append(current.right)
                current = current.left
            if current is None:
                current = stack.pop()

        return result
