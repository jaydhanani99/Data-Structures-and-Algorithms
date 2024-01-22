# https://practice.geeksforgeeks.org/problems/level-order-traversal/1

#User function Template for python3



class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        # Code here
        # Here we will follow iterative approach to find the level order traversal
        # For iterative approach we will use queue to track the current root nodes
        if not root:
            return []
            
        queue = [root]
        output = [root.data]
        
        while queue:
            current_root = queue.pop(0)
            if current_root.left:
                output.append(current_root.left.data)
                queue.append(current_root.left)
                
            if current_root.right:
                output.append(current_root.right.data)
                queue.append(current_root.right)
        return output