# https://www.interviewbit.com/old/problems/path-to-given-node/
# https://www.geeksforgeeks.org/print-path-root-given-node-binary-tree/

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def __init__(self):
        self.ans    =   []
        
    def traverse(self, root, x, path):
        path.append(root.val)
        if root.val == x:
            self.ans = path
            return
        
        if root.left:
            self.traverse(root.left, x, path.copy())
        if root.right:
            self.traverse(root.right, x, path.copy())
    
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root, x):
        # Iterative solution
        
        queue = [(root, [])]
        while queue:
            node, path = queue.pop(0)
            path.append(node.val)
            if node.val == x:
                return path
                
            if node.left:
                queue.append((node.left, path.copy()))
            if node.right:
                queue.append((node.right, path.copy()))
            
        
        
        # =========Recursive solution===========
        self.traverse(root, x, [])
        return self.ans