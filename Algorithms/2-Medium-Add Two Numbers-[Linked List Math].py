def node2number(pre, node):
    pre.append(node.val)
    if not node.next:
        pre.reverse()
        return pre
    else:
        return node2number(pre, node.next)
    
def number2node(d):
    nodes = [ListNode(int(i)) for i in str(d)]
    nodes.reverse()
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def addTwoNumbers(self, l1, l2):

        d1 = int("".join(str(d) for d in (node2number([], l1)))) 
        d2 = int("".join(str(d) for d in (node2number([], l2))))
        d3 = d1+d2
        
        return number2node(d3)

class Solution2:
    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)
        cur = root
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)

            cur.next = ListNode(val)
            cur = cur.next
            
        return root.next
            

if __name__ == "__main__":
    # Test Case
    l1 = number2node(342)
    l2 = number2node(465)

    sol = Solution1()
    l3 = sol.addTwoNumbers(l1, l2)
    print(node2number([], l3))
    