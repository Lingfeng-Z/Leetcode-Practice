class Solution():
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        elif n == 0:
            return 1
        else:
            return self.increasingmultiply(x, n)


    def increasingmultiply(self, a: int, b: int):
        x = a
        i = 1
        result = 1
        count = 0
        while True:
            result = result * a
            count += i
            if count == b:
                flag = 0
                break
            a = a * x
            i += 1
            if b - count < i:
                flag = 1
                break
        if flag == 0:
            return result
        else:
            result = result * self.increasingmultiply(x, b - count)
            return result

if __name__ == "__main__":
    Solu = Solution()
    ans = Solu.myPow(2, -2)
    print(ans)