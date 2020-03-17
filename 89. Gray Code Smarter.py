class Solution:
    def grayCode(self, n: int) -> list:
        ans = [0]
        for i in range(n):
            step = 1 << i
            temp = []
            for j in range(len(ans)-1, -1, -1):
                temp.append(ans[j]+step)
            ans.extend(temp)
        return ans

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.grayCode(3)
    print(result)