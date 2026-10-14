# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        hare = head
        tort = head

        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tort = tort.next

            if hare is tort:
                return True

        return False