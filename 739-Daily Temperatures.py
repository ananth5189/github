class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
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
            return -1
        x=self.top.val
        self.top=self.top.next
        return x
    def Peek(self):
        if self.top is None:
            return -1
        return self.top.val
    def IsEmpty(self):
        if self.top is None:
            return True
        return False
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=Stack()
        resarr=[0]*len(temperatures)
        a.Push(0)
        for i in range(1,len(temperatures)):
            while not(a.IsEmpty()) and temperatures[a.Peek()]<temperatures[i]:
                x=a.Pop()
                print(x)
                resarr[x]=(i-x)
            a.Push(i)
        return resarr
