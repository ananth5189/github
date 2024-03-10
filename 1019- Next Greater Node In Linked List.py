# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Stack:
    def __init__(self):
        self.top=None
    def Push(self,val):
        node=ListNode(val)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
    def Pop(self):
        if self.top is None:
            return [-1,-1]
        x=self.top.val
        self.top=self.top.next
        return x
    def Peek(self):
        if self.top is None:
            return [-1,-1]
        return self.top.val
    def IsEmpty(self):
        if self.top is None:
            return True
        return False
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp=head
        a=Stack()
        a.Push([0,temp.val])
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        temp=head.next
        resarr=[0]*count
        count=0
        print(resarr)
        while temp is not None:
            while not(a.IsEmpty()) and a.Peek()[1]<temp.val:
                x,y=a.Pop()
                resarr[x]=temp.val
            count+=1
            a.Push([count,temp.val])
            temp=temp.next
        return resarr
