# https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        