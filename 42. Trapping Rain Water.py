class Solution(object):
    def modifyCandidate(self, lis):
        i = 0
        flag = -1
        newr = []
        while i < len(lis):
            if lis[i] == 0:
                newr.append(lis[i])
                flag = 1
                i += 1
                continue
            if flag == -1:
                if i == 0:
                    newr.append(lis[i])
                elif lis[i] >= lis[i - 1]:
                    del (newr[-1])
                    newr.append(lis[i])
                else:
                    newr.append(lis[i])
            else:
                if lis[i] > lis[i - 1]:
                    newr.append(lis[i])
                else:
                    break
            i += 1
        return newr


    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        zero_in = []
        while i < len(height):
            if height[i] == 0:
                zero_in.append(i)
            i += 1
        candidates = []
        i = 0
        while i < len(zero_in):
            if i == 0 and zero_in[i] == 0:
                i += 1
                continue
            elif i == 0:
                candidates.append(height[0:zero_in[i + 1]])
            elif i == len(zero_in) - 1 and zero_in[i] == len(height):
                i += 1
                continue
            elif i == len(zero_in) - 1:
                candidates.append(height[zero_in[i - 1] + 1:len(height) + 1])
            else:
                candidates.append(height[zero_in[i - 1] + 1:zero_in[i + 1]])
            i += 1
        i = 0
        while i < len(candidates):
            candidates[i] = self.modifyCandidate(candidates[i])
            i += 1
        space = 0
        for i in candidates:
            max = min(i[0], i[-1])
            for x in i:
                if x > max:
                    continue
                else:
                    space += max-x
        print(space)

if __name__ == '__main__':
    s = Solution()
    s.trap([0,1,0,2,1,0,1,3,2,1,2,1])