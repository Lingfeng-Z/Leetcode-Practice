'''
@Descripttion: 
@version: 
@Author: Lingfeng Zhang
@Date: 2020-02-02
@LastEditors  : Lingfeng Zhang
@LastEditTime : 2020-02-02
'''

class Solution():
    def countPairs(self, numCount: int, ratingValues: list, target: int)->int:
        count = 0
        ratingValues.sort()
        for i in range(0, len(ratingValues)):
            for j in range(len(ratingValues)-1, i, -1):
                if i + j == target:
                    count += 1
                if i + j < target:
                    continue
        print(count)


if __name__ == "__main__":
    Solu = Solution()
    numcount = 10
    ratingvalues = [10, 3, 5, 7, 2, 8, 9, 6, 1, 4]
    target = 7
    Solu.countPairs(numcount, ratingvalues, target)