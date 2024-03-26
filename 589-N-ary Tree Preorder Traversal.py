"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        arr=[]
        arr.append(root.val)
        for i in root.children:
            arr.extend(self.preorder(i))
        return  arr
     
