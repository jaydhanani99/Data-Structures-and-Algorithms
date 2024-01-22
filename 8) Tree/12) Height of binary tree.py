# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def __init__(self):
        self.max_level = 0
        
    def traverse(self, root, level):
        if level > self.max_level:
            self.max_level = level
        
        if root.left:
            self.traverse(root.left, level+1)
        if root.right:
            self.traverse(root.right, level+1)
            
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.traverse(root, 1)
        return self.max_level