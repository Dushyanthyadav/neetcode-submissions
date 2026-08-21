# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def goodNode(node, max_value):
            nonlocal count
            if node == None:
                return
            if node.val >= max_value:
                count += 1
                max_value = node.val
            
            goodNode(node.left, max_value)
            goodNode(node.right, max_value)

        goodNode(root, root.val)

        return count