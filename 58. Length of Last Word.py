class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.strip().split(" ")
        if len(word_list) == 0:
            return ''
        else:
            return len(word_list[-1])


if __name__ == "__main__":
    Solu = Solution()
    Solu.lengthOfLastWord("a ")
