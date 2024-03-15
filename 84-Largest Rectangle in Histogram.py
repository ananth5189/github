class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def Push(self,val):
        node=Node(val)
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
    def largestRectangleArea(self, heights: List[int]) -> int:
        rightmin=[len(heights)]*len(heights)
        leftmin=[-1]*len(heights)
        st=Stack()
        for i in range(len(heights)):
            while not(st.IsEmpty()) and heights[st.Peek()]>heights[i]:
                rightmin[st.Pop()]=i
            st.Push(i)
        print(rightmin)
        heightsrev=heights[::-1]
        st=Stack()
        for i in range(len(heightsrev)):
            while not(st.IsEmpty()) and heightsrev[st.Peek()]>heightsrev[i]:
                leftmin[st.Pop()]=len(heights)-i-1
            st.Push(i)
        leftmin=leftmin[::-1]
        maxarea=0
        for i in range(len(heights)):
            maxarea=max(maxarea,(rightmin[i]-leftmin[i]-1)*heights[i])
        return maxarea
