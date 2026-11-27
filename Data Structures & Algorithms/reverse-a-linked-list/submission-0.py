# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or head.next==None:
            return head
        temp=head
        temp_stk=[]
        while(temp.next!=None):
            temp_stk.append(temp)
            temp=temp.next
        head=temp
        while(temp_stk):
            temp.next=temp_stk.pop()
            temp=temp.next
            temp.next=None
        return head