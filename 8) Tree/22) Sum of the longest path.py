# https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1

class Solution:
    def __init__(self):
        self.max_level = -1
        self.ans = 0
    def traverse(self, root, level, curr_sum):
        curr_sum += root.data
        
        if level > self.max_level:
            self.ans = curr_sum
            self.max_level = level
        elif level == self.max_level:
            self.ans = max(self.ans, curr_sum)
            
        if root.left:
            self.traverse(root.left, level+1, curr_sum)
        
        if root.right:
            self.traverse(root.right, level+1, curr_sum)
            
        
        
    def sumOfLongRootToLeafPath(self,root):
        if not root:
            return 0
        self.traverse(root, 0, 0)
        return self.ans