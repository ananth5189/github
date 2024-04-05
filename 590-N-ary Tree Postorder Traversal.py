"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def __init__(self):
      self.arr=[]
    def postorder(self, root: 'Node') -> List[int]:
      if root is None:
        return []
      for i in root.children:
        self.postorder(i)
      self.arr.append(root.val)
      return self.arr
        
          
      
        
