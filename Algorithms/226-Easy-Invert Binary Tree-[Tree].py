# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        else:
            # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root

class Solution:
        
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            if t1.left:
                self.mergeTrees(t1.left, t2.left)
            else:
                t1.left = t2.left
            if t1.right
                self.mergeTrees(t1.right, t2.right)
            else:
                t1.right = t2.right
        
            
        return t1