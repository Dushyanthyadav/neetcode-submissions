# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mylist = []
        for node in lists:
            while node != None:
                mylist.append(node)
                node = node.next
            
        sorted_list = sorted(mylist, key=lambda n: n.val)

        dummy = ListNode()
        a = dummy

        for node in sorted_list:
            a.next = node
            a = a.next
        
        return dummy.next