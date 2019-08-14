class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        candidate_pos = []
        string = ""
        dict_word = {}
        candidate = []
        new = []
        result = []
        if s == "" or words == []:
            return result
        for i in words:
            pos = self.findindex(i, s)
            if pos == []:
                return result
            if len(pos) == 1:
                candidate_pos.append(pos[0])
            else:
                dict_word[i] = pos
            string = string + i
        for x in candidate_pos:
            new = new + x
        candidate_pos = [new]
        for i in words:
            if i not in dict_word.keys():
                continue
            candidate = []
            for j in dict_word[i]:
                if candidate_pos == []:
                    candidate.append(j)
                else:
                    for x in candidate_pos:
                        if set(j).issubset(set(x)):
                            continue
                        else:
                            candidate.append((x + j))
            candidate_pos = candidate
        for x in candidate_pos:
            flag = 0
            x.sort()
            if x[-1] - x[0] != len(string) - 1:
                continue
            else:
                i = 1
                while i < len(x) - 1:
                    if x[i + 1] - x[i] != 1:
                        flag = 1
                        break
                    i += 2
                if flag == 0:
                    result.append(x[0])
        return list(set(result))

    def findindex(self, word, s):
        position = []
        i = 0
        while i < len(s):
            if len(s)-i < len(word):
                break
            if s[i] == word[0]:
                flag = 0
                j = 0
                while j < len(word):
                    if s[i + j] != word[j]:
                        flag = 1
                        break
                    j += 1
                if flag == 0:
                    position.append([i, i + j - 1])
            i += 1
        return position


if __name__ == "__main__":
    s = Solution()
    result = s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
    print(result)
