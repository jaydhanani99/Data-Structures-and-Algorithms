# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
    def traverse(self, root, level):
        if not root:
            return
        if len(self.output) <= level:
            self.output.append([root.val])
        else:
            self.output[level].append(root.val)
        
        self.traverse(root.left, level+1)
        self.traverse(root.right, level+1)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.traverse(root, 0)
        answer = []
        for x in self.output:
            answer.append(sum(x)/len(x))
        return answer