class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x2 = x
            rev = 0
            while x2 > 0:
                rev = (rev*10) + (x2%10)
                x2 //= 10
            return x == rev