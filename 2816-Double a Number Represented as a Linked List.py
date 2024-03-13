# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev=self.Reverse(head)
        restail=None
        carry=0
        temp=rev
        while temp is not None:
            doub=2*temp.val+carry
            temp.val=doub%10
            carry=doub//10
            restail=temp
            temp=temp.next
        if carry !=0:
            node=ListNode(carry)
            restail.next=node
        return self.Reverse(rev)
    def Reverse(self,head):
        if head is None:
            return head
        prev=None
        curr=head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
