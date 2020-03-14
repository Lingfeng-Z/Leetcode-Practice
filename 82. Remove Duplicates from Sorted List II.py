class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        past = ListNode(None)
        past.next = head
        new_head = past
        duplicate_val  = None
        while head.next is not None:
            if head.next.val == duplicate_val:
                head.next = head.next.next
                continue
            else:
                if head.val == head.next.val:
                    duplicate_val = head.val
                    head = past
                    continue
                past = head
                head = head.next
                if head is None:
                    break
        return new_head.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    Solu = Solution()
    Solu.deleteDuplicates(node1)