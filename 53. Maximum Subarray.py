class Solution:
    def maxSubArray(self, nums: list) -> int:
        '''
        @desciption: noob method
        @param {type}
        @return:
        '''
        max_v = sum(nums)
        max_array = []
        for i in range(len(nums), 0, -1):
            j = 0
            if i == 1:
                if max(nums) > max_v:
                    max_v = max(nums)
            else:
                while j+i <= len(nums):
                    now = nums[j:j+i]
                    if sum(now) > max_v:
                        max_v = sum(now)
                        max_array = now
                    j += 1
        print(max_array)

    def maxSubArrayFast(self, nums: list) -> int:
        max_v = nums[0]
        current_max = nums[0]
        for i in range(len(nums)):
            current_max = max(nums[i], current_max+nums[i])
            if current_max > max_v:
                max_v = current_max
        print(max_v)


if __name__ == "__main__":
    data = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
    Solu = Solution()
    Solu.maxSubArrayFast(data)
