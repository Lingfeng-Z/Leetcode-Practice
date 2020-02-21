class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] <= nums[i - 1]:
                i = i - 1
                continue
            else:
                break
        if i == 0:
            nums.sort()
        else:
            key_value = nums[i - 1]
            j = len(nums) - 1
            while j > i - 1:
                if nums[j] > nums[i - 1]:
                    nums[i - 1] = nums[j]
                    nums[j] = key_value
                    break
                j -= 1
            nums[i:len(nums)] = nums[len(nums) - 1:i - 1:-1]
