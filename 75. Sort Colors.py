class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        count_2= 0
        while i < len(nums):
            if nums[j] == 0:
                j += 1
            elif nums[j] == 1:
                nums.insert(len(nums)-count_2, nums[j])
                nums.remove(nums[j])
            else:
                nums.append(nums[j])
                nums.remove(nums[j])
                count_2 += 1
            i += 1
        print(nums)

if __name__ == "__main__":
    Solu = Solution()
    Solu.sortColors([,0])