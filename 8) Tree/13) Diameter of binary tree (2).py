# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

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
        
        # In answer we are not returning the number of node if it would number of path we should not do +1 here.
        self.ans = max(self.ans, left_level + right_level + 1)
        # Height of current node would be maximum height of left and right child + 1 (Which is the height of the root node itself)
        return 1 + max(left_level, right_level)
            
    def diameter(self, root):
        self.traverse(root)
        return self.ans