class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        a = a[::-1]
        b = b[::-1]
        if len(a) > len(b):
            min_length = len(b)
            max_length = len(a)
            longer = a
        else:
            min_length = len(a)
            max_length = len(b)
            longer = b
        i = 0
        forward = '0'
        while True:
            if i >= min_length and i < max_length:
                if forward == '0':
                    ans += longer[i:]
                    break
                elif forward == '1' and longer[i] == '1':
                    ans += '0'
                    forward = '1'
                else:
                    ans += '1'
                    forward = '0'
            elif i == max_length:
                if forward == '1':
                    ans += '1'
                    break
                else:
                    break
            else:
                can = [a[i], b[i], forward]
                one = can.count('1')
                if one == 0:
                    ans += '0'
                elif one == 1:
                    ans += '1'
                    forward = '0'
                elif one == 2:
                    ans += '0'
                    forward = '1'
                else:
                    ans += '1'
                    forward = '1'
            i += 1
        return ans[::-1]

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.addBinary("0", "0")
    print(result)