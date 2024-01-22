# https://www.interviewbit.com/old/problems/right-view-of-binary-tree/
# https://leetcode.com/problems/binary-tree-right-side-view/submissions/
# https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def __init__(self):
        self.output = []
        self.current_max_level = -1
        
    def traverse(self, root, level):
        # By using this condition we are ensuring that for each level,
        # we would have only one value which is the right child of the node
        # So basically we first call the right level, so that we have right child in output
        if self.current_max_level < level:
            self.output.append(root.val)
            self.current_max_level = level
        
        if root.right:
            self.traverse(root.right, level+1)
        
        if root.left:
            self.traverse(root.left, level+1)
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        if not root:
            return []
        
        # Recursive approach
        # self.traverse(root, 0)
        # return self.output
        
        # This is the iterative approach
        queue = [(root, 0)]
        output = []
        max_level = -1
        while queue:
            root, level = queue.pop(0)
            if max_level != level:
                output.append(root.val)
                max_level = level
            
            # We would add first right node as we required right view,
            # so right child would be popped first
            if root.right:
                queue.append((root.right, level+1))
                
            if root.left:
                queue.append((root.left, level+1))
            
        return output
        