# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()

        if head is None or head.next is None:
            return False

        curr = head
        while curr.next is not None:
            visit.add(curr)
            if curr.next and curr.next in visit:
                return True
            
            curr = curr.next
        

        return False
    
# Slow fast pointer solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        

        return False