# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        count=1
        #count is 1 since head is assumed to be already counted
        while count<k:
            count+=1
            temp=temp.next
        node1=temp
        node2=head
        while temp.next is not None:
            temp=temp.next
            node2=node2.next
        node1.val,node2.val=node2.val,node1.val
        return head
