# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # Depth first search, as soon as we hit the leaf, we will add our string to an array
        res = [0]


        def dfs(root, s):
            if not root.left and not root.right:
                res.append(int(s))
            
            if root.left:
                dfs(root.left, s + str(root.left.val))
            if root.right:
                dfs(root.right, s + str(root.right.val))
        
        dfs(root, str(root.val))
        return sum(res)

        