# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode("")
        node1 = ListNode("")
        node2 = ListNode("")
        array = []
        if list(set(lists)) == [None] or lists == []:
            return node1
        for i in lists:
            while 1:
                if i == None:
                    break
                array.append(i.val)
                i = i.next
        array.sort()
        if len(array[1:]) == 0:
            head.val = array[0]
            head.next = None
            node1 = head
        else:
            head.val = array[0]
            node1 = head
            head.next = node2
            head = node2
            node2 = ListNode("")
        loop = 0
        for i in array[1:]:
            head.val = i
            if loop == len(array)-2:
                head.next = None
            else:
                head.next = node2
            head = node2
            node2 = ListNode("")
            loop += 1
        return node1