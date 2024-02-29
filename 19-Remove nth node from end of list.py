# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr is not None:
            if self.lengthoflist(curr)==n:
                if curr==head:
                    head=head.next
                    curr=head
                else:
                    prev.next=curr.next
                    curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return head

    def lengthoflist(self,head):
        if head is None:
            return 0
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count
