class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        postion = m + n - 2
        need_to_fill = n - 1
        P_numerator = 1
        P_denominator = 1
        for i in range(1, need_to_fill+1):
            P_numerator = P_numerator * postion
            postion -= 1
            P_denominator = P_denominator * i
        return int(P_numerator / P_denominator)

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.uniquePaths(3, 3)
    print(result)