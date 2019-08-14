class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if nums == []:
                return 0
            i = 0
            while i < len(nums):
                if nums[i] >= target:
                    return i
                i += 1
            return len(nums)
