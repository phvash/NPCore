# Time:  O(n)
# Space: O(logn)
#
# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    head = None
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        current, length = head, 0
        while current is not None:
            current, length = current.next, length + 1
        self.head = head
        return self.sortedListToBSTRecu(0, length)
    
    def sortedListToBSTRecu(self, start, end):
        if start == end:
            return None
        mid = start + (end - start) / 2
        left = self.sortedListToBSTRecu(start, mid)
        current = TreeNode(self.head.val)
        current.left = left 
        self.head = self.head.next
        current.right = self.sortedListToBSTRecu(mid + 1, end)
        return current

if __name__ == "__main__":
    def pack(node, stop):
        for x in xrange(stop + 1):
            
            node.next = ListNode(x)
            
        return node

    # head = pack
    # head = ListNode(1)
    # pack(head, 10)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    head = ListNode(1)
    r = pack(head, 10)
    print(r.next)
    
    # result = Solution().sortedListToBST(head)
    # print result.val
    # print result.left.val
    # print result.right.val