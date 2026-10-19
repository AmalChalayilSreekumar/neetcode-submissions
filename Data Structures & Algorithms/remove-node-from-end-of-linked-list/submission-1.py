# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = head
        curr= head
        prev = None

        i = 0

        while counter!= None:
            i+=1
            counter = counter.next
        
        traverse = i-n

        if traverse == 0:
            return head.next

        while traverse>0:
            prev = curr
            curr = curr.next
            traverse-=1
        
        next_node = curr.next
        prev.next = next_node 
        
        return head


