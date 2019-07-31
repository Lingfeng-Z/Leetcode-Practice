# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        node2 = ListNode(None)
        node3 = ListNode(None)
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val<l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        node2 = head
        while(l1 != None and l2 != None):
            if l1.val < l2.val:
                node2.next = l1
                node2 = node2.next
                l1 = l1.next
            else:
                node2.next = l2
                node2 = node2.next
                l2 = l2.next
        if l1 == None:
            while(l2 != None):
                node2.next = l2
                node2 = node2.next
                l2 = l2.next
        else:
            while(l1 != None):
                node2.next = l1
                node2 = node2.next
                l1 = l1.next
        return head