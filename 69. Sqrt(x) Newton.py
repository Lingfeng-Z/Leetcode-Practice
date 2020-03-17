class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        guess = x
        ans = guess/2 + x/(2*guess)
        while abs(ans-guess) >= 1:
            guess = ans
            ans = guess/2 + x/(2*guess)
        return int(ans)



if __name__ == "__main__":
    Solu = Solution()
    result = Solu.mySqrt(3)
    print(result)