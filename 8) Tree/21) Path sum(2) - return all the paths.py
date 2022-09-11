# https://leetcode.com/problems/path-sum-ii/submissions/
# https://www.interviewbit.com/old/problems/root-to-leaf-paths-with-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans        =   []
        
    def findSum(self, root, sum, path):
    
        # Subtracting current val from sum
        # Now we check for this sum left or right subtree exists or not
        sum -=  root.val
        path.append(root.val)
        
        # if sum is zero and root is the leaf node then adding this path in final answer
        if sum == 0 and not root.left and not root.right:
            self.ans.append(path.copy())
            return
        
        # checking for remaining sum in left sub tree
        if root.left:
            self.findSum(root.left, sum, path.copy())
            
        # checking for remaining sum in right sub tree
        if root.right:
            self.findSum(root.right, sum, path.copy())
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.findSum(root, sum, [])
        return self.ans