import numpy as np

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = []
        char2num = {'(':1, ')':-1, '{':2, '}':-2, '[':3, ']':-3}
        for i in s:
            new_s.append(char2num[i])
        k = 0
        i = 1
        while(i < len(new_s)):
            if new_s[k] + new_s[i] == 0:
                del(new_s[k])
                del(new_s[k])
                k = 0
                i = 1
                continue
            k = i
            i += 1
        if len(new_s)!=0:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("[({(())}[()])]"))