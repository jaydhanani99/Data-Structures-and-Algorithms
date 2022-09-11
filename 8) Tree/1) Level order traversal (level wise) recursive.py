# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
        
    def traverse(self, root, level):
        # If this is true that means this level index does not exists in output
        # So we append the value so that index would be created
        if len(self.output) <= level:
            self.output.append([root.val])
        else:
            # If index already created we append this level value at level index
            self.output[level].append(root.val)
        
        if root.left:
            self.traverse(root.left, level+1)
        
        if root.right:
            self.traverse(root.right, level+1)
        
    def levelOrder(self, root):
        if not root:
            return []
        
        self.traverse(root, 0)
        return self.output