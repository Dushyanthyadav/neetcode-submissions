# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = head
        myset = set()
        myset.add(a)
        while a != None:
            if a.next in myset:
                return True
            myset.add(a.next)
            a = a.next
        
        return False
        