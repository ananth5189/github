# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        if temp1 is None:
            return temp2
        if temp2 is None:
            return temp1
        temp1=list1
        temp2=list2
        reshead=None
        restail=None
        while temp1 is not None and temp2 is not None:
            if temp1.val<temp2.val:
                node=ListNode(temp1.val)
                temp1=temp1.next
            else:
                node=ListNode(temp2.val)
                temp2=temp2.next
            if reshead is None:
                reshead=node
                restail=node
            else:
                restail.next=node
                restail=node
        if temp1 is None:
            restail.next=temp2
        if temp2 is None:
            restail.next=temp1
        return reshead

