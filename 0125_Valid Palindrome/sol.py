class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        check = True
        while check and i <j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower()!= s[j].lower():
                check = False
            else:
                i += 1
                j -= 1
        return check