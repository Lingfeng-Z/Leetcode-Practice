class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        ans = []
        for i in self.findIPAddress(s, 9, 3):
            ans.append(".".join(i))
        return ans
    
    def findIPAddress(self, s: str, length_lim_right: int, length_lim_left: int):
        ans = []
        for i in range(1,4):
            current_string = s[:i]
            if len(current_string) > 1 and current_string[0] == '0':
                continue
            current = [s[:i]]
            remaining = s[i:]
            if len(remaining) > length_lim_right or len(remaining) < length_lim_left or int(current_string) > 255:
                continue
            else:
                if len(remaining) == 0:
                    return [current]
                else:
                    ans.extend([current+j for j in self.findIPAddress(remaining, length_lim_right-3, length_lim_left-1) if len(j) != 0])
        return ans
            



if __name__ == "__main__":
    Solu = Solution()
    result = Solu.restoreIpAddresses("0000")
    print(result)