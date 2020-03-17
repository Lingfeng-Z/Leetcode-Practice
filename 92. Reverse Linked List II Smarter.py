class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        virtual_head = ListNode(None)
        virtual_head.next = head
        new_head = virtual_head
        i = 0
        last_node = None
        while new_head is not None:
            next_head = new_head.next
            if i == m-1:
                link_list_sep = new_head
                reverse_now = new_head.next
                new_head = new_head.next
            elif i >= m and i <= n:
                new_head.next = last_node
                last_node = new_head
                new_head = next_head
                if i == n:
                    link_list_sep.next = last_node
                    reverse_now.next = new_head
            else:
                new_head = new_head.next
            i += 1
        return virtual_head.next




if __name__ == "__main__":
    Solu = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    Solu.reverseBetween(node1, 1, 5)