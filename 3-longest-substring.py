class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding Window
        visit = {}
        l = 0
        res = 0

        for r in range(len(s)):
            # Store the values in hashmap
            if s[r] in visit and visit[s[r]] >= l:
                l = visit[s[r]] + 1

            else:
                res = max(res, r - l + 1)
            
            visit[s[r]] = r
        
        return res

