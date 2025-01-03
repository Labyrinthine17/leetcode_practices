class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        s_len = len(s)
        t_len = len(t)
            
        while i < s_len and j < t_len:
            # print("i",i,"j",j)
            # print("s[i]",s[i],"t[j]",t[j],'\n')
            if s[i] == t[j]:
                i += 1
            j += 1

        return(i == s_len)