# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        temp1=head
        prev=None
        if head is None or head.next is None:
            return None
        while temp.next is not None and temp1.next is not None:
            if count%2==0:
                prev=temp
                temp=temp.next
                temp1=temp1.next
            else:
                temp1=temp1.next
            count+=1
        prev.next=temp.next            
        return head
        
#alternative solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast=slow=head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head


