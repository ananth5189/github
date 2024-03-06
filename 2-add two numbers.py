# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        car=0
        temp1=l1
        temp2=l2
        reshead=None
        restail=None
        while temp1 is not None or temp2 is not None:
            if temp1 is not None and temp2 is not None:
                sum=car+(temp1.val+temp2.val)
            elif temp1 is not None and temp2 is None:
                sum=car+(temp1.val)
            elif temp1 is None and temp2 is not None:
                sum=car+(temp2.val)
            node=ListNode(sum%10)
            car=sum//10
            if reshead is None:
                reshead=node
                restail=node
            else:
                restail.next=node
                restail=node
            if temp1 is not None:
                temp1=temp1.next
            if temp2 is not None:
                temp2=temp2.next   
        if car:
            node=ListNode(car)
            restail.next=node
            restail=car
        return reshead
