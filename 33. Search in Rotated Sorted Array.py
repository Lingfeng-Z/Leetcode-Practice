'''
@Descripttion: 
@version: 
@Author: Lingfeng Zhang
@Date: 2020-01-24
@LastEditors  : Lingfeng Zhang
@LastEditTime : 2020-01-25
'''
class Solution:
    def search(self, nums: list, target: int) -> int:
        if target not in nums:
            return -1
        stan = sorted(nums)
        mv = len(nums)-self.stepSearch(nums, stan)
        length = len(stan)
        left = 0
        right = length-1
        while True:
            i = int((left+right)/2)
            if stan[i] < target:
                left = i+1
            elif stan[i] > target:
                right = i-1
            else:
                break
        if i+mv >= len(nums):
            return i+mv-len(nums)
        else:
            return i+mv

    def stepSearch(self, nums: list, stan: list):
        length = len(nums)
        left = 0
        right = length-1
        while True:
            i = int((left+right)/2)
            if nums[0] < stan[i]:
                right = i-1
            elif nums[0] > stan[i]:
                left = i+1
            else:
                break
        return i

if __name__ == "__main__":
    Solu = Solution()
    array = [3,4,5,6,1,2]
    mokuhyou = 2
    index = Solu.search(array, mokuhyou)
    print("最终index是:{}".format(index))