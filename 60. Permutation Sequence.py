class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        data = [i for i in range(1, n+1)]
        return self.searchAns(data, k)
    
    def searchAns(self, num_set: list, k: int) -> str:
        num_instance_each_number = 1
        if len(num_set) != 0:
            for i in range(len(num_set)-1, 0, -1):
                num_instance_each_number = num_instance_each_number * i
            currentposition_num = num_set[int((k-1)/num_instance_each_number)]
            num_set.remove(currentposition_num)
            new_k = k%num_instance_each_number if k%num_instance_each_number !=0 else num_instance_each_number
            return str(currentposition_num) + self.searchAns(num_set, new_k)
        else:
            return ""
        

if __name__ == "__main__":
    Solu = Solution()
    output = Solu.getPermutation(4, 6)
    print(output)