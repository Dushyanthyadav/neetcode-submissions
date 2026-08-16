# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mylist = []
        cur = head

        while cur != None:
            mylist.append(cur)
            cur = cur.next
        
        i = len(mylist) - n
        del mylist[i]
        dummy = ListNode()
        a = dummy
        for node in mylist:
            a.next = node
            a = a.next

        a.next = None

        return dummy.next
