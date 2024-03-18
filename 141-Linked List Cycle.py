# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=[]
        temp=head
        while temp is not None:
            if temp in visited:
                return True
            visited.append(temp)
            temp=temp.next
        return False
        
