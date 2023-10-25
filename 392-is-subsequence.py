class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub, main = 0, 0 


        while main < len(t) and sub < len(s):
            if t[main] == s[sub]:
                sub += 1
            main += 1

        return sub == len(s)


