class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def Push(self,val):
        node=Node(val)
        if self.front is None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
    def Pop(self):
        if self.front is None:
            return -1
        x=self.front.val
        self.front=self.front.next
        return x
    def IsEmpty(self):
        if self.front is None:
            return True
        return False
    def Peek(self):
        if self.front is None:
            return -1
        return self.front.val
class MyStack:
    def __init__(self):
        self.st1=Queue()
        self.st2=Queue()
    def push(self, x: int) -> None:
        self.st2.Push(x)   
        while not(self.st1.IsEmpty()) :
            self.st2.Push(self.st1.Pop())
        tempst=self.st1
        self.st1=self.st2
        self.st2=tempst
    def pop(self) -> int:
        return self.st1.Pop()
    def top(self) -> int:
        return self.st1.Peek()
    def empty(self) -> bool:
        return self.st1.IsEmpty()
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
