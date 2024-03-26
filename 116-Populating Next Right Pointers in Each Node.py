"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from queue import Queue
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
      q=Queue()
      q.put(root)
      if root is None:
        return root
      while q.qsize()!=0:
        prev=None
        for i in range(q.qsize()):
          node=q.get()
          node.next=prev
          prev=node
          if node.right is not None:
            q.put(node.right)
          if node.left is not None:
            q.put(node.left)
      return root
          
      
        
