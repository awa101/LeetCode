# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(node):
            if not node:
                return None
            elif node.val == target.val:
                return node

            return dfs(node.left) or dfs(node.right)

        return dfs(cloned)