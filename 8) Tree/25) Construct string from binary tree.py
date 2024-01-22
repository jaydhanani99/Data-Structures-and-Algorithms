# https://leetcode.com/problems/construct-string-from-binary-tree/
# https://www.geeksforgeeks.org/binary-tree-string-brackets/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        # Initially left and right string would be ''
        # It would be a case when root does not have left and right child
        left_string = ''
        right_string = ''
        
        if root.left:
            # find the left string using recursive function
            left_string = '('+self.traverse(root.left)+')'
        
        if root.right:
            # if left string is empty and right child is exists we set left string as ()
            if left_string == '':
                left_string = '()'
            # find the right string using recursive function
            right_string = '('+self.traverse(root.right)+')'
        
        # Returning answer in format root(left)(right)
        return str(root.val)+left_string+right_string
        
        
        
    def tree2str(self, root: TreeNode) -> str:
        return self.traverse(root)