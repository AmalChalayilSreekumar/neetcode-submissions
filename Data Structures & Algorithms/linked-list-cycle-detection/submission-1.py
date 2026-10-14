# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        if head is None: 
            return False

        
        rabbit = head
        hare = head

        while rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            hare = hare.next
            if rabbit is hare:
                return True
    
        return False