class Solution:
    '''
    Time Limit Exceeded
    def canJump(self, nums: list) -> bool:
        if len(nums) == 1:
            return True
        queue = [0]
        history = []
        while len(queue) != 0:
            temp = queue.pop(0)
            history.append(temp)
            queue.extend([i for i in range(temp+1, min(temp+nums[temp]+1,len(nums))) if i not in queue and i not in history])
            if len(nums)-1 in queue:
                return True
        return False
    '''

    
    #O(n)
    def canJump(self, nums: list) -> bool:
        if len(nums) == 1:
            return True
        low = 0
        high = 0
        possible = [low, high]
        for i in range(len(nums)-1):
            high = max(i+nums[i], high)
            low = i + 1
            if high >= len(nums)-1:
                return True
            if high < low:
                return False
        return False
    
    def canJump2(self, nums: list) -> bool:
        lo = hi = 0
        while hi < len(nums)-1:
            if hi == max(i+nums[i] for i in range(lo, hi+1)):
                return False
            else:
                lo, hi = hi+1, max(i+nums[i] for i in range(lo, hi+1))
        return True


if __name__ == "__main__":
    Solu = Solution()
    print(Solu.canJump([0]))
    print(Solu.canJump2([0]))
