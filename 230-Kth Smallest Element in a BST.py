# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=self.Traversal(root)
        arr.sort()
        return arr[k-1]
    def Traversal(self,root):
        if root is None:
            return []
        arr=[]
        arr.append(root.val)
        arr.extend(self.Traversal(root.left))
        arr.extend(self.Traversal(root.right))
        return arr
            
        
