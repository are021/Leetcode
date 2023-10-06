# class Trie:

#     def __init__(self):
#         self.trie = {}

#     def insert(self, word: str) -> None:

#         def insertTrie(ch_index, map):
#             if word[ch_index] not in map:
#                 map[word[ch_index]] = {}
#             if ch_index == len(word) - 1:
#                 map[word[ch_index]]["null"] = 0
#                 return 0
#             return insertTrie(ch_index + 1, map[word[ch_index]])
        
#         insertTrie(0, self.trie)
            
#     def search(self, word: str) -> bool:

#         def searchTrie(ch_index,map):
#             if ch_index == len(word) - 1:
#                 if "null" not in map[word[ch_index]]:
#                     return False
#                 return True
#             if word[ch_index] not in map[word[ch_index]]
            

        

#     def startsWith(self, prefix: str) -> bool:


        


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['*']=''
            
    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True if '*' in curr else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True

        