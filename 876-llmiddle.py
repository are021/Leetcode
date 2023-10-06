# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #2 passes

        N = 0

        curr = head

        while curr:
            N += 1
            curr = curr.next

        curr = head
        N = N // 2

        while N > 0:
            N -= 1
            curr = curr.next
        
        return curr
    
'''
2 pointer solution
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 2 pointers

        curr = head

        while curr and curr.next:
            head = head.next
            curr = curr.next.next
        return head