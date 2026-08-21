# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def side(node, depth):
            if not node:
                return

            depth += 1
            if depth > len(res):
                res.append(node.val)
            
            side(node.right, depth)
            side(node.left, depth)

        side(root, 0)

        return res