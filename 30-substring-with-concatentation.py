# My Crazy Solution!
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_map = {}
        word_len = len(words[0])
        num_of_words = len(words)

        res = []

        for word in words:
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1


        l, r = 0, (word_len * num_of_words) - 1

        while r < len(s):
            curr_visited = {}
            valid = True
            for left in range(l, r + 1, word_len):
                curr = s[left : left + word_len]
                if curr in word_map:
                    # Check the word count matches that in curr visited
                    if curr in curr_visited and curr_visited[curr] < word_map[curr]:
                        curr_visited[curr] += 1
                    elif curr not in curr_visited:
                        curr_visited[curr] = 1

            if curr_visited == word_map:
                res.append(l)

            l += 1
            r += 1

        
        return res
        
            
# Better Optimized Solution

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_map = {}
        word_len = len(words[0])
        n = len(words)
        words_len = word_len * n
        res = []

        for word in words:
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1


        #Sliding Window
        # We don't need to go to the end of string, until the final word
        for l in range(len(s) - words_len + 1):
            curr_visited = {}

            for r in range(n):
                word_idx = l + r * word_len

                curr = s[word_idx : word_idx + word_len]

                if curr not in word_map:
                    break
                
                curr_visited[curr] = curr_visited.get(curr, 0) + 1

                if curr_visited[curr] > word_map[curr]:
                    break

            if curr_visited == word_map:
                res.append(l)
        
        return res
            