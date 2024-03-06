# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l, r = 0, 0 
        def depthFunction(node):
            if not node:
                return 0
            l = 1 + depthFunction(node.left)
            r = 1 + depthFunction(node.right)
            return max(l, r)

        return depthFunction(root)

        

        
            
# Other solutions

def maxDepth() -> int:
    if not root:
        return 0
    level = 0
    q = deque([root])


while q:
    for i in range(len(q)):
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    level += 1
        

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))