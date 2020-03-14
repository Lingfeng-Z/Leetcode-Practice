class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        past = None
        count = 0
        while i < len(nums):
            if past is None:
                past = nums[i]
                count = 1
            else:
                if nums[i] == past:
                    if count == 2:
                        nums.remove(nums[i])
                        continue
                    else:
                        count += 1
                else:
                    count = 1
                    past = nums[i]
            i += 1
        return len(nums)

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.removeDuplicates([1,1,1,2,2,3])
    print(result)

