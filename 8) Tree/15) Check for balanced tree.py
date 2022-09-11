# https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
# https://leetcode.com/problems/balanced-binary-tree/submissions/
# https://www.interviewbit.com/old/problems/balanced-binary-tree/

class Solution:
    def traverse(self, root):
        # If not root that means it is either left/right child of leaf node which is None, so it's height is 0
        if not root:
            return 0

        # Finding the level/height of the left child
        left_level = self.traverse(root.left)
        # Finding the level/height of the right child
        right_level = self.traverse(root.right)
        
        # if absolute difference between left and right level is more than 1 that means it's not balanced tree
        # In such a case we would return None
        # also if we encountered left_level or right_level as None that means we have returned None in previous function calls
        # If we are returning None that means it's not balanced tree
        if left_level is None or right_level is None or abs(left_level - right_level) > 1:
            return None
        
        return 1 + max(left_level, right_level)
    
    def isBalanced(self, root: TreeNode) -> bool:
        # If we are returning None that means it's not balanced tree
        return 0 if self.traverse(root) is None else 1