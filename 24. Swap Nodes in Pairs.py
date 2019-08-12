# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode("")
        node1 = ListNode("")
        node2 = ListNode("")
        if head == None:
            return head
        if head.next == None:
            return head
        else:
            node.val = head.next.val
            node.next = ListNode("")
            node1 = node
            node = node.next
            node.val = head.val
            head = head.next
            if head.next == None:
                node.next = None
                return node1
            else:
                head = head.next
                node.next = ListNode("")
                node = node.next
        while 1:
            if head.next == None:
                flag = 2
                break
            node.val = head.next.val
            node.next = ListNode("")
            node = node.next
            node.val = head.val
            head = head.next
            if head.next == None:
                flag = 1
                break
            flag = 2
            head = head.next
            node.next = ListNode("")
            node = node.next
        if flag == 1:
            node.next = None
        else:
            node.val = head.val
            node.next = None
        return node1

