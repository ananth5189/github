# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict={}
        temp=head
        while temp is not None:
            if temp.val not in dict.keys():
                dict[temp.val]=1
            else:
                dict[temp.val]+=1
            temp=temp.next
        reshead=None
        restail=None
        for i,j in dict.items():
            if j<=1:
                node=ListNode(i)
                if reshead is None:
                    reshead=node
                    restail=node
                else:
                    restail.next=node
                    restail=node
        return reshead
