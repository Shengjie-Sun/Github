# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def recursivor(left, right):
            if left > right:
                return None
            # Inorder Traversal: Always Choose Left Middle Node as a Root
            # always choose left middle node as a root
            idx = (left+right) // 2
            
            # inorder traversal: left -> node -> right
            root = TreeNode(nums[idx])
            root.left = recursivor(left, idx-1)
            root.right = recursivor(idx+1, right)
            
            return root
        
        left, right = 0, len(nums)-1
        
        return recursivor(left, right)