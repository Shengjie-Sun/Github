# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.BALANCED = True
        
    def isBalanced(self, root: TreeNode) -> bool:
        
        def recursivor(root):
            if not root:
                return 0
            else:
                left = recursivor(root.left)
                right = recursivor(root.right)
                if abs(right-left) >= 2:
                    self.BALANCED = False
                return max(left, right) + 1
        
        recursivor(root)
        
        return self.BALANCED