# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
      if root is None:
        return []
      q=Queue()
      q.put(root)
      resarr=[]
      while q.qsize()!=0:
        maxval=float('-inf')
        for i in range(q.qsize()):
          node=q.get()
          maxval=max(maxval,node.val)
          if node.left is not None:
            q.put(node.left)
          if node.right is not None:
            q.put(node.right)
        resarr.append(maxval)
      return resarr
          
          
          
        
