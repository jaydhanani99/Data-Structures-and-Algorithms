# https://www.interviewbit.com/old/problems/invert-the-binary-tree/
# https://leetcode.com/problems/invert-binary-tree/submissions/

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # To invert the tree we just need to swap the right and left child of the every node
        # Here we would spaw the node itself instead of the value so that their child elements would not get changed
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        # Which returns the actuall root node itself at last
        return root