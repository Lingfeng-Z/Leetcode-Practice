class Solution:
    def generateParenthesis(self, n: int):
        self.left = n
        self.right = n
        link = ['(']
        self.selection = ['(', ")"]
        self.candidate = []
        self.findCandi(link)
        print(self.candidate)

    def findCandi(self, head):
        x = head[:]
        for i in self.selection:
            x.append(i)
            flag = self.classification(x)
            if flag == 0:
                x = x[:-1]
                continue
            elif flag == 1:
                for q in range(self.left+self.right-len(x)):
                    x.append(')')
                self.candidate.append("".join(x))
                x = head[:]
            else:
                self.findCandi(x)
                x = head[:]

    def classification(self, x: list):
        num_left = x.count('(')
        num_right = x.count(')')
        if num_right > num_left or num_left > self.left:
            return 0
        elif num_left == self.left and num_right <= self.right:
            return 1
        else:
            return 2


if __name__ == "__main__":
    Solu = Solution()
    Solu.generateParenthesis(3)