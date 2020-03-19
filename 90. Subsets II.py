class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        ans = [[]]
        for i in nums:
            candidate = []
            for j in ans:
                temp = j.copy()
                temp.append(i)
                temp.sort()
                if temp not in ans:
                    candidate.append(temp)
            ans.extend(candidate)
        return ans
            


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.subsetsWithDup([1,2,2])
    print(result)