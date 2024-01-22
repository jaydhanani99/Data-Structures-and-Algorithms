# https://leetcode.com/problems/path-sum/submissions/
# https://www.interviewbit.com/problems/path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
    
        # ============= Recursive solution ================
        # Subtracting current val from sum
        # Now we check for this sum left or right subtree exists or not
        sum -=  root.val
        
        # if sum is zero and root is the leaf node then return True
        if sum == 0 and not root.left and not root.right:
            return True
        
        # checking for this sum in left sub tree
        if root.left and self.hasPathSum(root.left, sum):
            return True
            
        # checking for this sum in right sub tree
        if root.right and self.hasPathSum(root.right, sum):
            return True
        
        return False
    
        
        # =========== Iterative solution =================
        queue = [(root, 0)]
        
        while queue:
            node, curr_sum = queue.pop(0)
            curr_sum += node.val
            
            if curr_sum == sum and not node.left and not node.right:
                return True
            if node.left:
                queue.append((node.left, curr_sum))
            if node.right:
                queue.append((node.right, curr_sum))
        return False
            