# https://leetcode.com/problems/cousins-in-binary-tree/
# https://www.geeksforgeeks.org/check-two-nodes-cousins-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class InputNode:
    def __init__(self, val):
        self.val = val
        self.depth = None
        self.parent_val = None
        
class Solution:
    def __init__(self):
        self.x = None
        self.y = None
    
    def traverse(self, root, level):
        # if current node value is equal to the x node value
        if root.val == self.x.val:
            # storing the depth
            self.x.depth = level
            # storing the parent node value of current node
            self.x.parent_val = root.parent_val
        
        # if current node value is equal to the y node value
        if root.val == self.y.val:
            # storing the depth
            self.y.depth = level
            # storing the parent node value of current node
            self.y.parent_val = root.parent_val
            
        if root.left:
            # if current node has left child then setting the child node parent value as current node value
            root.left.parent_val = root.val
            self.traverse(root.left, level+1)
            
        if root.right:
            # if current node has right child then setting the child node parent value as current node value
            root.right.parent_val = root.val
            self.traverse(root.right, level+1)
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Considering parent value of root node as -1
        root.parent_val = -1
        # We have created InputNode custom class which holds value, depth and parent node value as properties
        self.x = InputNode(x)
        self.y = InputNode(y)
        
        self.traverse(root, 0)
        
        if self.x.depth == self.y.depth and self.x.parent_val != self.y.parent_val:
            return True
        return False