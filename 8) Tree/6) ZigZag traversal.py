# https://www.interviewbit.com/old/problems/zigzag-level-order-traversal-bt/
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1

class Solution:
    def __init__(self):
        self.output    =   []
        
    def traverse(self, root, level):
        # If this is true that means this level index does not exists in output
        # So we append the value so that index would be created
        if len(self.output) <= level:
            self.output.append([root.val])
        else:
            # Now we have two options
            # If level is even (we are considering level starting from 0) we store in normal order
            # If level is odd we store in reverse order
            if level % 2 == 0:
                self.output[level].append(root.val)
            else:
                self.output[level].insert(0, root.val)
        
        if root.left:
            self.traverse(root.left, level+1)
        
        if root.right:
            self.traverse(root.right, level+1)
            
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        self.traverse(root, 0)
        return self.output