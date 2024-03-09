class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,val):
        node=ListNode(val)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
    def pop(self):
        if self.top is None:
            return -1
        x=self.top.val
        self.top=self.top.next
        return x
    def Isempty(self):
        if self.top is None:
            return True
        return False
    def Peek(self):
        if self.top is None:
            return -1
        return self.top.val   
    def printStack(self):
        if self.top is None:
            return -1
        temp=self.top
        while temp is not None:
            print(temp.val)
            temp=temp.next         
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr=[-1]*len(nums)
        a=Stack()
        a.push(0)
        for i in range(1,len(nums)*2):
            while not(a.Isempty()) and nums[a.Peek()]<nums[i%len(nums)]:
                arr[a.pop()]=nums[i%(len(nums))]
            a.push(i%len(nums))
        return arr
