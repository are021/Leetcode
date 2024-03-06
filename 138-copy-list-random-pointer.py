"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memo = { None : None }

        curr = head

        # Create node map

        while curr:
            copy = Node(curr.val)
            memo[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = memo[curr]
            copy.next = memo[curr.next]
            copy.random = memo[curr.random]
            curr = curr.next
        return memo[head]

# Intuitive O(1) solution 
# (7) -> (7* (clone)) -> 8 -> 8*
# 2nd pass - fill in random pointers curr.next.random = curr.random.next (the clone of the original random node)
# 3rd pass - restore lists
# 