# https://leetcode.com/problems/binary-tree-paths/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
    def traverse(self, root, path):
        # Adding current node to current path
        path.append(str(root.val))
        
        # If it is child node then adding this path as final path
        if not root.left and not root.right:
            self.paths.append('->'.join(path))
        
        
        if root.left:
            self.traverse(root.left, path.copy())
        if root.right:
            self.traverse(root.right, path.copy())
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
    
        # This is the recursive approach we can also do iterative approach using queue
        self.traverse(root, [])
        return self.paths