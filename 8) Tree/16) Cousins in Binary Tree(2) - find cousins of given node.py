# https://www.interviewbit.com/old/problems/cousins-in-binary-tree/
# https://www.geeksforgeeks.org/print-cousins-of-a-given-node-in-binary-tree/

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def __init__(self):
        # Which stores node of each level
        self.level_mapping = {}
        self.x = None
        self.x_level = None
        self.x_parent_val = None
        
    def traverse(self, root, level):
        # if element found we store element level and their parent value
        if root.val == self.x:
            self.x_level = level
            self.x_parent_val = root.parent_val
            
        # Storing current node in current level key of level_mapping
        if level not in self.level_mapping:
            self.level_mapping[level] = [root]
        else:
            self.level_mapping[level].append(root)
        
        if root.left:
            # Storing parent_val of left child
            root.left.parent_val = root.val
            self.traverse(root.left, level+1)
            
        if root.right:
            # Storing parent_val of right child
            root.right.parent_val = root.val
            self.traverse(root.right, level+1)
        
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root, x):
        # Iterative solution
        queue = [root]
        bln_element_found = 0
        while queue and bln_element_found == 0:
            # This is the length of queue without considering it's child elements
            # as we have not added the child of queue elements as of now
            length_without_child = len(queue)
            
            # length_without_child is because if we encounter our element in either left or right child,
            # we pop the parent elements which was already in queue and,
            # we add all the child elements in queue except the founded element's,
            # left or right sibling
            while length_without_child > 0:
                current_node = queue.pop(0)
                
                # if we found element in either left or right sibling we would not add current left or right child
                if (current_node.left and current_node.left.val == x) or (current_node.right and current_node.right.val == x):
                    bln_element_found = 1
                else:
                    # else we would add left or right child
                    if current_node.left:
                        queue.append(current_node.left)
                    
                    if current_node.right:
                        queue.append(current_node.right)
                
                # which removes the current parent elements and,
                # bln_element_found == 0 condition of outer while loop,
                # would stop adding next child elements
                length_without_child -= 1
        
        # Now we have Cousins of x in queue
        output = []
        
        for element in queue:
            output.append(element.val)
        return output
        
        # ===================== Recursive solution ==================
        self.x = x
        root.parent_val = -1
        self.traverse(root, 0)
        
        # That means element is not found
        if self.x_level not in self.level_mapping:
            return []
        
        output = []
        # we traverse through all the elements at level = x_level and,
        # add only those elements which parent are different than the x_parent
        for x in self.level_mapping[self.x_level]:
            if x.parent_val != self.x_parent_val:
                output.append(x.val)
        return output