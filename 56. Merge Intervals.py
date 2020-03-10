class Solution:
    def merge(self, intervals: list):
        if len(intervals) == 0:
            return []
        intervals.sort()
        candidate = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > candidate[-1][1]:
                candidate.append(intervals[i])
            else:
                candidate[-1] = [candidate[-1][0], max(candidate[-1][1], intervals[i][1])]
        return candidate




if __name__ == "__main__":
    Solu = Solution()
    result = Solu.merge([[2,6],[1,3],[8,10],[15,18]])
    print(result)