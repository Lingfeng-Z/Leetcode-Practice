class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i-1] += 1
            else:
                break
        return digits

    def plusOneMoe(self, digits: List[int]) -> List[int]:
        '''
        @desciption: trash
        @param {type} 
        @return: 
        '''
        digits = [str(num) for num in digits]
        str0 = "".join(digits)
        return [x for x in str(int(str0)+1)]