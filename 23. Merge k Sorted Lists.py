# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import numpy as np


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode("")
        node1 = ListNode("")
        infi = float("inf")
        if list(set(lists)) == [None] or lists == []:
            return node1
        array = []
        for x in lists:
            if x != None:
                array.append(x.val)
            else:
                array.append(infi)
        m = np.argmin(array)
        node1 = lists[m]
        lists[m] = lists[m].next
        head = node1
        while 1:
            array = []
            for x in lists:
                if x != None:
                    array.append(x.val)
                else:
                    array.append(infi)
            m = np.argmin(array)
            if list(set(array)) == [infi]:
                head.next = None
                break
            head.next = lists[m]
            head = head.next
            lists[m] = lists[m].next
        return node1
