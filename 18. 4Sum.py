class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        solution = []
        new_num = []
        result = []
        for i, j in enumerate(nums):
            if j >= target & target>0:
                break
            three_sum_target = target-j
            new_num = nums[i + 1:]
            for q, l in enumerate(new_num):
                res = new_num[q+1:]
                two_sum_target = three_sum_target-l
                result = self.twosum(res, two_sum_target)
                if result is None:
                    continue
                for k in result:
                    k.insert(0, l)
                    k.insert(0, j)
                    solution.append(k)
        solution = list(set([tuple(t) for t in solution]))
        solution = [list(t) for t in solution]
        return solution

    def twosum(self, nums, target):
        solution = []
        new_num = []
        result = []
        for i, j in enumerate(nums):
            if j > target & target>0:
                break
            one_sum_target = target - j
            new_num = nums[i + 1:]
            if one_sum_target in new_num:
                result = [j, one_sum_target]
            else:
                continue
            solution.append(result)
        solution = list(set([tuple(t) for t in solution]))
        solution = [list(t) for t in solution]
        return solution

if __name__ == "__main__":
    sol = Solution()
    array = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.fourSum(array,target))