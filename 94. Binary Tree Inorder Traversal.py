class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        if root is None:
            return []
        ans = [root.val]
        queue = [root]
        position_list = [root]
        while len(queue) != 0:
            current_node = queue.pop(0)
            current_position = position_list.index(current_node)
            left_son = current_node.left
            right_son = current_node.right
            if left_son is not None:
                queue.append(left_son)
                position_list.insert(current_position, left_son)
                ans.insert(current_position, left_son.val)
            if right_son is not None:
                queue.append(right_son)
                position_list.insert(position_list.index(current_node) + 1, right_son)
                ans.insert(position_list.index(current_node) + 1, right_son.val)
        return ans

                


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    Solu = Solution()
    result = Solu.inorderTraversal(node1)
    print(result)
