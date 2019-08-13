class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        i = 0
        j = 0
        m = 1
        while i < len(haystack):
            if haystack[i] == needle[0]:
                if i + len(needle) > len(haystack):
                    return -1
                while j < len(needle):
                    if haystack[i+j] != needle[j]:
                        j = 0
                        m = 0
                        break
                    j += 1
                if m == 0:
                    m = 1
                    i += 1
                else:
                    return i
            else:
                i += 1
        return -1

if __name__ == "__main__":
    s = Solution()
    result = s.strStr("mississippi", "issip")
    print(result)