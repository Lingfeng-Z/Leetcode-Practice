class TreeNode():
    def __init__(self, data):
        self.data = data
        self.visited = False


    def __str__(self):
        return str(self.data)

    def sonNode(self, left, right):
        self.left = TreeNode(None)
        self.right = TreeNode(None)
        self.left.data = left
        self.right.data = right

class TreeMethods():
    def makeselfTree(self, point: TreeNode, depth: int, limit: int, history: list):
        localdepth = depth
        localhis = history[:]
        localhis.append(point.data)
        localhis_future = [localhis+[i] for i in ['(',')']]
        if localdepth == 1:
            point.sonNode(None, None)
            point.left.visited = True
            point.right.visited = True
        else:
            if localhis_future[0].count('(') > limit:
                point.sonNode(None, ')')
                point.left.visited = True
                localdepth -= 1
            elif localhis_future[1].count(')') > localhis_future[1].count('('):
                point.sonNode('(', None)
                point.right.visited = True
                localdepth -=1
            else:
                point.sonNode('(',')')
                localdepth -= 1
            if point.left.data != None:
                self.makeselfTree(point.left, localdepth, limit, localhis)
            if point.right.data != None:
                self.makeselfTree(point.right, localdepth, limit, localhis)

    def traversalTree(self, head: TreeNode):
        self.candidate = []
        stack = []
        data = []
        stack.append(head)
        head.visited = True
        while stack != []:
            currentpoint = stack[-1]
            if currentpoint.left.data == None and currentpoint.right.data == None:
                self.candidate.append("".join([x.data for x in stack]))
                stack = stack[:-1]
            if False in [currentpoint.left.visited, currentpoint.right.visited]:
                for i in [currentpoint.left, currentpoint.right]:
                    if i.visited == False:
                        i.visited =True
                        stack.append(i)
                        break
            else:
                stack = stack[:-1]


class Solution:
    def generateParenthesis(self, n: int):
        root_point = TreeNode('(')
        MakeTree = TreeMethods()
        MakeTree.makeselfTree(root_point, 2*n, n, [])
        MakeTree.traversalTree(root_point)
        print(MakeTree.candidate)




if __name__ == "__main__":
    S = Solution()
    S.generateParenthesis(6)
