class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) < 2:
            return len(nums)
        while 1:
            if i == len(nums)-1:
                break
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                continue
            i = i + 1
        return len(nums)