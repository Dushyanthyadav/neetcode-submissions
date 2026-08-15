# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        a = dummy
        pointer = head
        mylst = []
        while pointer != None:
            mylst.append(pointer)
            pointer = pointer.next

        i = 0
        j = len(mylst) - 1

        while i < j:
            a.next = mylst[i]
            a = a.next
            a.next = mylst[j]
            a = a.next
            i += 1
            j -= 1
        
        if len(mylst) % 2 != 0:
            a.next = mylst[i]
            a = a.next
            a.next = None
        else:
            a.next = None

        