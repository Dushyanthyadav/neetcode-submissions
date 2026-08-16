# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, mult1 = 0, 1
        while l1:
            num1 += l1.val * mult1
            mult1 *= 10
            l1 = l1.next

        num2, mult2 = 0, 1
        while l2:
            num2 += l2.val * mult2
            mult2 *= 10
            l2 = l2.next

        res = num1 + num2
        if res == 0:
            return ListNode(0)

        dummy = ListNode()
        curr = dummy
        while res > 0:
            curr.next = ListNode(res % 10)
            curr = curr.next
            res //= 10

        return dummy.next


