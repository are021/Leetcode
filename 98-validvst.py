# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        
        def dfs (curr):
            #Base case
            l, r = None, None
            if curr is None:
                return
            if curr.left and curr.left.val >= curr.val:
                return False
            if curr.right and curr.right.val <= curr.val:
                return False
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            if l == False or r == False:
                return False
            return True
        
        return dfs(root)
    

#Construct bst for testing

val = TreeNode(
    val=5,
    left=TreeNode(val=5),
    right=TreeNode(val=6,left=TreeNode(3), right=TreeNode(7))
)


x = Solution().isValidBST(val)