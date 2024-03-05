# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list=self.listtoarr(head)
        list.sort()
        temp=head
        i=0
        while temp is not None:
            temp.val=list[i]
            i+=1
            temp=temp.next
        return head
    def listtoarr(self,head):
        if head is None:
            return []
        arr=[]
        temp=head
        while temp is not None:
            arr.append(temp.val)
            temp=temp.next
        return arr
