class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i = len(num2) - 1
        sum_all = 0
        while i >= 0:
            k = int(num2[i])
            sum_temp = 0
            j = len(num1) - 1
            while j >= 0:
                sum_temp += int(str(int(num1[j]) * k) + '0' * (len(num1) - j - 1))
                j -= 1
            sum_all += int(str(sum_temp) + '0' * (len(num2) - i - 1))
            i -= 1
        return str(sum_all)