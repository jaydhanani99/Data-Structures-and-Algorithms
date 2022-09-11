# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

class Solution:
    def getLeaf(self, root, leaf):
        if not root.left and not root.right:
            leaf.append(root.data)
        
        if root.left:
            self.getLeaf(root.left, leaf)
        if root.right:
            self.getLeaf(root.right, leaf)
        return leaf
        
    def getLeft(self, root, left):
        if root:
            # In both condition we add the value first so that order would be in ascending order level wise
            # if left child is exists then left child itself is the part of the left outer tree
            if root.left:
                left.append(root.data)
                self.getLeft(root.left, left)
            # if left child is not exists that means right child is the part of the left outer tree
            elif root.right:
                left.append(root.data)
                self.getLeft(root.right, left)
        return left
        
    def getRight(self, root, right):
        if root:
            # In both condition we add the value after the function call so that order would be in descending order level wise
            # if right child is exists then right child itself is the part of the right outer tree
            if root.right:
                self.getRight(root.right, right)
                right.append(root.data)
            # if right child is not exists that means left child is the part of the right outer tree
            elif root.left:
                self.getRight(root.left, right)
                right.append(root.data)
        return right
        
    def printBoundaryView(self, root):
        if not root:
            return []
        # Ansewer would start from root and traverse from left outer tree, leaf nodes and right outer tree
        # So first we add the root node value
        # then we traverse through left outer tree and add those value except the leaf node
        # then we traverse through tree and add the leaf nodes from left to right
        # then we traverse through right outer tree and add those value except the leaf node
        # for the right outer tree answer would be in reverse order
        return [root.data]+self.getLeft(root.left, [])+self.getLeaf(root, [])+self.getRight(root.right, [])