class Solution:
    def simplifyPath(self, path: str) -> str:
        while True:
            if '//' not in path:
                break
            path = path.replace('//','/')
        path = path.strip('/')
        candidate = ['/'+i for i in path.split('/')]
        stack = []
        for i in candidate:
            if i == '/.':
                continue
            elif i == '/..':
                stack = stack[:-1]
            else:
                stack.append(i)
        if len(stack) == 0:
            return '/'
        else:
            return "".join(stack)


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.simplifyPath('/home//foo/')
    print(result)