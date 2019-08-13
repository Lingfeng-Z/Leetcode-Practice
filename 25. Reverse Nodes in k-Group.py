# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        i = 0
        node1 = ListNode("")
        while 1:
            node2, new_head = self.reverseK(head, k)
            node1 = self.cat(node1, node2)
            head = new_head
            if head == None:
                break
            i += 1
        return node1

    def reverseK(self, head, k):
        node = ListNode("")
        i = 0
        lastNode = self.telllastNode(head, k)
        if lastNode == -1:
            return head, None
        while i < k:
            node = head
            head = head.next
            node.next = lastNode
            lastNode = node
            if i == k - 1:
                node1 = node
            i += 1
        return node1, head

    def telllastNode(self, head, k):
        i = 0
        node = head
        while i < k:
            if node.next == None and i != k - 1:
                return -1
            if node.next == None and i == k - 1:
                return None
            node = node.next
            i += 1
        return None

    def cat(self, head1, head2):
        if head1.val == "":
            return head2
        node4 = head1
        while 1:
            if head1.next == None:
                head1.next = head2
                return node4
            head1 = head1.next