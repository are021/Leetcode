# My solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverseMapping = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):

            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            
            if t[i] in reverseMapping:
                if mapping[t[i]] != s[i]:
                    return False


            if s[i] not in mapping:
                mapping[s[i]] = t[i]

            if t[i] not in reverseMapping:
                reverseMapping[t[i]] = s[i]

        
        return True

        # You can also iterate through a string by zipping it
        # for c1, c2 in zip(s,t)