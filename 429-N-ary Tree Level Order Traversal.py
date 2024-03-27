"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import Queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
      if root is None:
        return []
      q=Queue()
      q.put(root)
      resarr=[]
      while q.qsize()!=0:
        arr=[]
        for i in range(q.qsize()):
          node=q.get()
          arr.append(node.val)
          for j in node.children:
            q.put(j)
        resarr.append(arr)
      return resarr
            
          
