class Solution:
    def subsets(self, nums: list):
        self.ans = []
        data = nums
        for i in range(0, len(data)+1):
            self.findPath([], data, i)
        return self.ans

    def findPath(self, pathnow, candidate, lim):
        if lim == 0:
            self.ans.append([])
        elif lim == 1:
            for j in candidate:
                temp_path = pathnow.copy()
                temp_path.append(j)
                self.ans.append(temp_path)
        else:
            temppath = pathnow.copy()
            temppath.append(candidate[0])
            self.findPath(temppath, candidate[1:], lim-1)
            if len(candidate) >= lim:
                self.findPath(pathnow, candidate[1:], lim)


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.subsets([1,2,3])
    print(result)