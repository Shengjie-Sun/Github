# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
        
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            t1.val += t2.val
            if t1.left:
                self.mergeTrees(t1.left, t2.left)
            else:
                t1.left = t2.left
            if t1.right:
                self.mergeTrees(t1.right, t2.right)
            else:
                t1.right = t2.right
        elif t2:
            return t2

        return t1

class Solution2:
        
    def mergeTrees(self, t1, t2):
        
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1