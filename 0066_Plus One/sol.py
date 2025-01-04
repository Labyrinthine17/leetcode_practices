class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        increment = 1

        while i >= 0:
            num = digits[i] + increment
            if num == 10:
                digits[i] = 0
                increment = 1
            else:
                digits[i] = num
                increment = 0
            i -= 1    

        if increment:
            digits = [1] + digits

        return digits