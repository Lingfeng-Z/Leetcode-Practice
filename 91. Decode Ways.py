class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if int(s) <= 26:
            if int(s) > 10 and int(s) != 20:
                return 2
            else:
                return 1
        else:
            if int(s[:2]) <= 26:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.numDecodings("9343746637672651697474472872418916594371213618363875622963812845376142981965514145661441836865837899")
    print(result)