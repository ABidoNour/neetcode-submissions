# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,curr_max,curr_min):
            if node is None:
                return True
            if not curr_min < node.val < curr_max:
                return False
            return dfs(node.left, node.val, curr_min) and dfs(node.right,curr_max,node.val)
        return dfs(root,float('inf'),float('-inf'))