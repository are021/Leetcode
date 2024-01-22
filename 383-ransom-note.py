from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomMap = {}

        for ch in ransomNote:
            if ch not in ransomMap:
                ransomMap[ch] = 1
            else:
                ransomMap[ch] += 1
        
        # Pass through the magazine
        # If zero, remove from hashmap

        for ch in magazine:
            if ch in ransomMap:
                ransomMap[ch] -= 1

                if ransomMap[ch] == 0:
                    del ransomMap[ch]

        return len(ransomMap) == 0
    

# We can use a counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False