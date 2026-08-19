# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(a, b):
            if a and b == None:
                return False
            if b and a == None:
                return False

            if a == None and b == None:
                return True
            
            if a.val != b.val:
                return False

            if a.left == None and b.left:
                return False
            if a.left and b.left == None:
                return False
            if a.right == None and b.right:
                return False
            if a.right and b.right == None:
                return False

            if a.right == b.right and a.left == b.left:
                return True

            right = True
            left = True
            if a.right and b.right:
                right = dfs(a.right, b.right)
            if a.left and b.left:
                left = dfs(a.left, b.left)
            
            return right and left
        
        return dfs(p, q)
            
 