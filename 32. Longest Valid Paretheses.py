class Solution:
    '''
    brute force
    '''
    def bruteForceLongestValidParentheses(self, s: str) -> int:
        max_pare = 0
        i = 2
        while i <= len(s):
            for k in range(0, len(s)-i+1):
                mark = self.classifyParentheses(s[k:k+i])
                if mark == 0:
                    max_pare = i
                    break
                else:
                    continue
            if max_pare == 0:
                return 0
            i += 2
        return max_pare
    
    def classifyParentheses(self, s: str):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return 1
                else:
                    stack = stack[:-1]
        if len(stack) == 0:
            return 0
        else:
            return 1

    def dpLongestValidParetheses(self, s:str):
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                if i-2 >= 0:
                    dp[i] = dp[i-2]+2
                else:
                    dp[i] = 2
            if s[i] == ')' and s[i-1] == ')':
                if s[i-dp[i-1]-1] == '(' and i-dp[i-1]-1 >= 0:
                    if i-dp[i-1]-2 >= 0:
                        dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                    else:
                        dp[i] = dp[i-1]+2
        return max(dp)

if __name__ == "__main__":
    Solu = Solution()
    targetstring = "(()))())("
    Result = Solu.dpLongestValidParetheses(targetstring)
    print(Result)