class Solution:
    def search(self, nums: list, target: int) -> bool:
        if len(nums) == 0:
            return False
        stan = sorted(nums)
        mv = len(nums)-self.stepSearch(nums, stan)
        length = len(stan)
        left = 0
        right = length-1
        while True:
            i = int((left+right)/2)
            if stan[i] < target:
                if left >= right:
                    return False
                left = i+1
            elif stan[i] > target:
                if left >= right:
                    return False
                right = i-1
            else:
                return True
        return False

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
    array = [1,1]
    number = 0
    result = Solu.search(array, number)
    print(result)