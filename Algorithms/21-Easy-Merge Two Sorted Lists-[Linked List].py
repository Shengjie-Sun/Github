def node2number(pre, node):
    pre.append(node.val)
    if not node.next:
        return pre
    else:
        return node2number(pre, node.next)
    
def number2node(d):
    nodes = [ListNode(int(i)) for i in str(d)]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归
class Solution1:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

class Solution2:
    def mergeTwoLists(self, l1, l2):
        root = ListNode("#")
        cur = root

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        
        return root.next

            

if __name__ == "__main__":
    l1 = number2node(124)
    l2 = number2node(134)

    sol = Solution2()
    l3 = sol.mergeTwoLists(l1, l2)
    print(node2number([], l3))
    