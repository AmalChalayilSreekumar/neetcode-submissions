# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Curr = l1
        l2Curr = l2
        final = ListNode(None)
        tail = final
        carry = False

        while l1Curr or l2Curr or carry:

            if l2Curr is None and l1Curr is None:
                tail.next = ListNode(1)
                break
            if l1Curr is None:
                currSum = l2Curr.val
                l2Curr = l2Curr.next
            elif l2Curr is None:
                currSum = l1Curr.val
                l1Curr = l1Curr.next
            else:
                currSum = l1Curr.val + l2Curr.val
                l1Curr = l1Curr.next
                l2Curr = l2Curr.next

            if carry:
                currSum += 1

            if currSum > 9:
                currSum -= 10
                carry = True
            else:
                carry = False

            tail.next = ListNode(currSum)
            tail = tail.next

        return final.next