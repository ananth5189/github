# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list=self.list(head)
        return list==list[::-1]
    def list(self,head):
        if head is None:
            return []
        temp=head
        arr=[]
        while temp is not None:
            arr.append(temp.val)
            temp=temp.next
        return arr

        
