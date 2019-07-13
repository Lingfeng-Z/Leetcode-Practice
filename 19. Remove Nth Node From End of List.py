# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        node = head
        i = 1
        j = 0
        while (node.next != None):
            node = node.next
            i += 1
        target = i - n
        node0 = ListNode(head.val)
        node1 = ListNode(head.val)
        node0 = head
        node1 = head
        while (j != target):
            node0 = node1
            node1 = node1.next
            j += 1
        if node0 == node1:
            return head.next
        else:
            node0.next = node1.next
            return head