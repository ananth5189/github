# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=self.Length(head)
        if head is None or k==0 or length==k:
            return head
        temp1=temp2=head
        while temp1.next is not None:
            temp1=temp1.next
        temp1.next=head
        count=0
        while count != (length-k%length):
            count+=1
            head=head.next
        while temp2.next !=head:
            temp2=temp2.next
        temp2.next=None
        return head

    def Length(self,head):
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        return count
