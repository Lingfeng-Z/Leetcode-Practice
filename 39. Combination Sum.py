class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutionset = self.combination(candidates, target)
        return solutionset

    def combination(self, candidates, target):
        solutionset = []
        candidates = [x for x in candidates if x <= target]
        candidates.sort(reverse=True)
        i = 0
        while i < len(candidates):
            solution = []
            select = candidates[i]
            solution = [select]
            candidate = candidates[i:]
            target_new = target - select
            if target_new == 0:
                solutionset.append(solution)
                solution = []
            elif target_new < candidate[-1]:
                solution = []
                continue
            else:
                solution.extend(self.combination(candidate, target_new))
        return solutionset

if __name__ == "__main__":
    s = Solution()
    s.combinationSum([2,3,6,7], 7)
