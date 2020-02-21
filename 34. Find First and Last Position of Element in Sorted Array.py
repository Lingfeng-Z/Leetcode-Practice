class Solution:
    def searchRange(self, nums: list, target: int):
        if target not in nums:
            return [-1, -1]
        left = 0
        right = len(nums)-1
        while True:
            i = int((left+right)/2)
            if nums[i] < target:
                left = i + 1
            elif nums[i] > target:
                right = i - 1
            else:
                break
        one_pos_position = i
        starting = self.left_first_element(one_pos_position, nums)
        ending = self.right_first_element(one_pos_position, nums)
        return [starting, ending]
    
    def left_first_element(self, live_position: int, nums: list):
        left = 0
        right = live_position
        while True:
            i = int((left+right)/2)
            if nums[live_position-i] == nums[live_position]:
                left = i+1
                if left > right:
                    return live_position-i
            elif nums[live_position-i] < nums[live_position] and nums[live_position-i+1] == nums[live_position]:
                break
            else:
                right = i-1
        return live_position-i+1

    def right_first_element(self, live_position: int, nums: list):
        left = 0
        right = len(nums)-live_position-1
        while True:
            i = int((left+right)/2)
            if nums[live_position+i] == nums[live_position]:
                left = i+1
                if left > right:
                    return live_position+i
            elif nums[live_position+i] > nums[live_position] and nums[live_position+i-1] == nums[live_position]:
                break
            else:
                right = i-1
        return live_position+i-1


if __name__ == "__main__":
    Solu = Solution()
    array = [1]
    mokuhyou = 1
    index = Solu.searchRange(array, mokuhyou)
    print("最终index是:{}".format(index))