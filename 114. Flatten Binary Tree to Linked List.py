# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    node_vec = None
    
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        return self.preorder(root)
        
    def preorder(self,node: 'TreeNode') -> 'None':
        if not node:
            return
        
        self.preorder(node.right)
        self.preorder(node.left)
        
        node.right = self.node_vec
        node.left  = None   
        self.node_vec = node
        
