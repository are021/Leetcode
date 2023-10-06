# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         balanced = True
#         def dfs(node):
#             if not node:
#                 return -1
            
#             l = dfs(node.left)
#             r = dfs(node.right)

#             if abs(l - r) > 1:
#                 balanced = False
#             return max(1 + l, 1 + r)

#         dfs(root)
#         return balanced

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            
            l = dfs(node.left)
            r = dfs(node.right)
            balanced =  l[0] and r[0] and abs( l[1] - r[1]) <= 1
            return [balanced, 1 + max(l[1], r[1])]

        return dfs(root)[0]
    

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            if (abs(l - r) > 1 or l == -1 or r == -1):
                return -1
            return 1 + max(l, r)

        return False if dfs(root) == -1 else True