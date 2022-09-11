# https://www.interviewbit.com/old/problems/reverse-level-order/

class Solution:
    def __init__(self):
        self.output    =   []
    def traverse(self, root, level):
        # If this is true that means this level index does not exists in output
        # So we append the value so that index would be created
        # We can use dictonary too to store level wise data
        if len(self.output) <= level:
            self.output.append([root.val])
        else:
            # If index already created we append this level value at level index
            self.output[level].append(root.val)
        
        if root.left:
            self.traverse(root.left, level+1)
        
        if root.right:
            self.traverse(root.right, level+1)
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        self.traverse(root, 0)
                
        ans         =   []
        maxLevel    =   len(self.output)
        for i in range(maxLevel-1, -1, -1):
            ans +=  self.output[i]
        return ans
