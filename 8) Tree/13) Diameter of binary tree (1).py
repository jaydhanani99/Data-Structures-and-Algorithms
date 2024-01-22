# https://leetcode.com/problems/diameter-of-binary-tree/submissions/

class Solution:
    def __init__(self):
        self.ans = 0
        
    def traverse(self, root):
        # If not root that means it is either left/right child of leaf node which is None
        if not root:
            return 0

        # Finding the level of the left child
        left_level = self.traverse(root.left)
        # Finding the level of the right child
        right_level = self.traverse(root.right)
        
        # In answer we are not returning the number of node in this path instead we are returning path count that's why we have not done +1 here
        self.ans = max(self.ans, left_level + right_level)
        # Height of current node would be maximum height of left and right child + 1 (Which is the height of the root node itself)
        return 1 + max(left_level, right_level)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.ans