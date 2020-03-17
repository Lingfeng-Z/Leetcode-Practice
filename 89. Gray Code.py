class Solution:
    def grayCode(self, n: int) -> list:
        visited = []
        visited.append("".join(['0' for i in range(n)]))
        ans = [0]
        limit = n
        while len(visited) < 2 ** n:
            current = visited[-1]
            current_list = list(current)
            connect = []
            for i in range(n):
                temp = current_list.copy()
                if temp[i] == '0':
                    temp[i] = '1'
                else:
                    temp[i] = '0'
                if "".join(temp) not in visited:
                    connect = temp
                    break
            connect_string = "".join(connect)
            visited.append(connect_string)
            ans.append(int('0b'+connect_string, 2))
        return ans
            
            
if __name__ == "__main__":
    Solu = Solution()
    result = Solu.grayCode(10)
    print(result)