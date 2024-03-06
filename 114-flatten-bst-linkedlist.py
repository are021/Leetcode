# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Move left subtree right and flatten
        curr = root
        while curr:
            if curr.left:
                store = curr.left
                while store.right:
                    store = store.right
                
                # Found successor
                    
                store.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorder_flatten(root)
    
    def preorder_flatten(self, root):
        if not root:
            return None
        
        left, right = self.preorder_flatten(root.left), self.preorder_flatten(root.right)

        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
        
        return right or left or root










            