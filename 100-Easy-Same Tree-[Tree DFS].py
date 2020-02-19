# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def __init__(self):
        self.SAME = True
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p and q:
            if p.val == q.val:
                self.isSameTree(p.left, q.left)
                self.isSameTree(p.right, q.right)
            else:
                self.SAME = False
        elif p or q:
            self.SAME = False
            
        return self.SAME

class Solution2:        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        elif p or q:
            return False
            
        return True