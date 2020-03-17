class Solution:
    def numDecodings(self, s: str) -> int:
        dp = []
        for i in range(len(s)-1, -1, -1):
            if i == len(s)-1:
                if s[i] == '0':
                    dp.append(0)
                else:
                    dp.append(1)
            elif i == len(s)-2:
                if s[i] == '0':
                    dp.append(0)
                elif int(s[i:]) <= 26:
                    if int(s[i:]) > 10 and int(s[i:]) != 20:
                        dp.append(2)
                    else:
                        dp.append(1)
                else:
                    dp.append(dp[-1])
            else:
                if s[i] == '0':
                    dp.append(0)
                elif int(s[i:i+2]) <= 26:
                        dp.append(dp[-1]+dp[-2])
                else:
                    dp.append(dp[-1])
        return dp[-1]

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.numDecodings("002")
    print(result)