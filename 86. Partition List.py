class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = ListNode(None)
        head2 = ListNode(None)
        new_head1 = head1
        new_head2 = head2
        while head is not None:
            if head.val < x:
                head1.next = head
                head1 = head1.next
            else:
                head2.next = head
                head2 = head2.next
            head = head.next
        head2.next = None
        head1.next = new_head2.next
        return new_head1.next


if __name__ == "__main__":
    Solu = Solution()
    node1 = ListNode(3)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(0)
    node7 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    result = Solu.partition(node1,3)