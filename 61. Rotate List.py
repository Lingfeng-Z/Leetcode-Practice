class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0 or head.next == None:
            return head
        last_head = head
        num = 1
        while last_head.next != None:
            last_head = last_head.next
            num += 1
        if num < k:
            k = k % num
            if k == 0:
                return head
        position = num - k + 1
        last_head.next = head
        last_head = head
        i = 1
        while last_head.next != head:
            if i == position:
                break
            last_head = last_head.next
            i += 1
        head = last_head
        last_head = head
        while last_head.next != head:
            last_head = last_head.next
        last_head.next = None
        return head


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
    Solu.rotateRight(node1, 2)