class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            
            if nums[lo] < nums[mid]:
                if target < nums[lo] or target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            elif nums[lo] > nums[mid]:
                if target < nums[mid] or target > nums[hi]:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                lo += 1
        return False