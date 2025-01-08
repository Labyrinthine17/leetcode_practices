class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = {}

        for i in magazine:
            if i in magazine_letters:
                magazine_letters[i] += 1
            else:
                magazine_letters[i] = 1

        for j in ransomNote:
            if j in magazine_letters:
                magazine_letters[j] -= 1
                if magazine_letters[j] < 0:
                    return False
            else:
                return False
            
        return True