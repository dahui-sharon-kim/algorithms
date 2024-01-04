# https://leetcode.com/problems/same-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        print(p.val, q.val)
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

sol = Solution()
tn1 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3, TreeNode(4)))
tn2 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3, TreeNode(5)))
print(sol.isSameTree(tn1, tn2))