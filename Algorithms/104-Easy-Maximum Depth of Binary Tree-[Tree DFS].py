# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(1, root)]
        dtp_max = 0
        
        while stack:
            dtp_cur, node = stack.pop()
            # 不要忘了这一句!
            if node is not None:
                dtp_max = max(dtp_max, dtp_cur)
                stack.append((dtp_cur+1, node.right))
                stack.append((dtp_cur+1, node.left))
        
        return dtp_max