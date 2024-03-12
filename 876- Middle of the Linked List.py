# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head
        temp1=head
        while temp1 is not None and temp1.next is not None:
            temp=temp.next
            temp1=temp1.next.next
        return temp

        
