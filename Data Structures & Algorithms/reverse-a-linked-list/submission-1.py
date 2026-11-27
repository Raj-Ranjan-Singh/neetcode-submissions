# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or head.next==None:
            return head
        prev=None;new_head=head;curr=copy.copy(head)
        while(new_head):
            curr.next=prev
            prev=curr
            new_head=new_head.next
            curr=copy.copy(new_head)
        return prev