# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         stack = deque()  
#         for c in s:
#             if c.isalnum():
#                 print(c)
#                 stack.append(c.lower())     
        
#         for c in s:
#             if c.isalnum():
#                 val = stack.pop()
#                 if c.lower() != val:
#                     return False
#         return True


# 2 pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        if len(s) == 1:
            return True

        while l < r:
            if (s[l].isalnum() and s[r].isalnum()):
                if (s[l].lower() != s[r].lower()):
                    return False
                else:
                    l += 1
                    r -= 1
            
            if not s[l].isalnum():
                l += 1

            if not s[r].isalnum():
                r -= 1

        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed = ""

        for c in s:
            if c.isalnum():
                fixed += c.lower()
        
        l, r = 0, len(fixed) - 1

        while l <= r:
            if fixed[l] != fixed[r]:
                return False
            
            l += 1
            r -= 1
        return True

            

