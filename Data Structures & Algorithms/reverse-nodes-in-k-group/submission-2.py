# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        newHead = None
        prevTail = None
        groupHead = head

        while groupHead:
            current = groupHead
            count = 1

            while current and count < k:
                current = current.next
                count += 1

            if not current:                  # fewer than k nodes left: leave them as-is
                if prevTail:
                    prevTail.next = groupHead
                else:
                    newHead = groupHead      # list shorter than k overall
                break

            secondPart = current.next
            current.next = None

            current = groupHead
            prevStart = None

            while current:
                nextL = current.next
                current.next = prevStart
                prevStart = current
                current = nextL
            # prevStart = new head of this group, groupHead = new tail

            if prevTail:
                prevTail.next = prevStart    # connect previous group to this one
            else:
                newHead = prevStart          # first group decides the final head

            prevTail = groupHead
            groupHead = secondPart

        return newHead




















