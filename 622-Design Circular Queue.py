from collections import deque
class MyCircularQueue:
    def __init__(self, k: int):
        self.deque=deque()
        self.k=k
    def enQueue(self, value: int) -> bool:
        if len(self.deque)>=self.k:
            return False
        self.deque.append(value)
        return True
    def deQueue(self) -> bool:
        if len(self.deque)==0:
            return False
        self.deque.popleft()
        return True
    def Front(self) -> int:
        if len(self.deque)==0:
            return -1
        return self.deque[0]
    def Rear(self) -> int:
        if len(self.deque)==0:
            return -1
        return self.deque[-1]
    def isEmpty(self) -> bool:
        return len(self.deque)==0
    def isFull(self) -> bool:
        return len(self.deque)==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
