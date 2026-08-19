# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(a, b):
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
                right = same(a.right, b.right)
            if a.left and b.left:
                left = same(a.left, b.left)
            
            return right and left

        def traverse(root, subroot):
            if root is not None:
                if root.val == subroot.val and same(root, subroot):
                        return True
                    

                return traverse(root.right, subroot) or traverse(root.left, subroot)
            return False

        return traverse(root, subRoot)


            














