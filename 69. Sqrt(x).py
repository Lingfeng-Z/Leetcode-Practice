class Solution:
    def mySqrt(self, x: int) -> int:
        seq = 1
        i = 0
        j = 0
        past_i = i
        while True:
            if i > x and past_i <= x:
                j -= 1
                break
            else:
                past_i = i
                i += seq
                j += 1
                seq += 2
        return j
    
    #应该用牛顿法求解https://blog.csdn.net/BlueBlueSkyZ/article/details/88373117

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.mySqrt(10)
    print(result)