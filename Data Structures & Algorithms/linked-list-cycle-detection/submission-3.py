# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        s1=head;s2=copy.copy(head)
        while(s1.next and s2 and s2.next):
            if(s1==s2):
                return True
            s1=s1.next;s2=s2.next.next
        return False