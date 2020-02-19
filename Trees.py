# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BinaryTree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = []
    while q:
        node = queue.pop(0)
        if node is not None:
            node.left = nodes.pop(0)
            node.right = nodes.pop(0)
            queue.append[node.left]
            queue.append[node.right]
    
    return root

if __name__ == "__main__":
    # Test Case
    node = [1,2,3]

    tree = BinaryTree(node)
    print(tree)


        
