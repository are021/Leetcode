# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        res = root

        def recurTree(node):

            if node is None:
                return
            left, right = node.left, node.right
            
            node.right, node.left = left, right 

            recurTree(node.right)
            recurTree(node.left)
        recurTree(res)
        return res
            