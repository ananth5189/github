class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.tail=None
    def push(self,data):
        newnode=node(data)
        if self.top is None:
            self.top=newnode
            self.tail=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None: return '$'
        x=self.top.data
        self.top=self.top.next
        return x
    def peek(self):
        if self.top is None:
            return '$'
        else:
            return self.top.data
    def matched(self,data1,data2):
        if data1=='(' and data2==')':
            return 1
        elif data1=='{' and data2=='}':
            return 1
        elif data1=='[' and data2==']':
            return 1
        else:
            return 0
    def isempty(self):
        if self.top is None:
            return 1
        return 0
class Solution:
    def isValid(self, s: str) -> bool:
        b=Stack()
        for i in s:
            if i in ['(','{','[']:
                b.push(i)
            #elif b.isempty():
            #    return 0
            elif b.matched(b.peek(),i):
                b.pop()
            else:
                return 0
        if b.isempty():
                return 1
        return 0
