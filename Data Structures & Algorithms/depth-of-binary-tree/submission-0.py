# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return self.depth

        return self.rec(root, self.depth)
    
    def rec(self, root, dep):
        if root == None:
            return dep
        new_depth = dep + 1
        left_dep = self.rec(root.left, new_depth)
        right_dep = self.rec(root.right, new_depth)
        depth = max(left_dep, right_dep)

        return depth