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
    def IsEmpty(self):
        if self.top is None:
            return True
        return False
    def Peek(self):
        if self.top is None:
            return -1
        return self.top.val    

class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[]
        rightmax=[]
        st=Stack()
        st.Push(height[0])
        for i in height:
            if st.Peek()>i:
                leftmax.append(st.Peek())
            else:
                st.Push(i)
                leftmax.append(i)
        heightrev=height[::-1]
        st=Stack()
        st.Push(heightrev[0])
        for i in heightrev:
            if st.Peek()>=i:
                rightmax.append(st.Peek())
            else:
                st.Push(i)
                rightmax.append(i)
        rightmax=rightmax[::-1]
        sum=0
        for i in range(len(height)):
            sum+=min(leftmax[i],rightmax[i])-height[i]
        return sum
