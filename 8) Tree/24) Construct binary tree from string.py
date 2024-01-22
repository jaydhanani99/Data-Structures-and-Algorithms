# https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/
# https://www.lintcode.com/problem/880/

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def findClosingIndex(self, string, startIndex):
        total_length = len(string)
        total_open_bracket = 1
        for i in range(startIndex+1, total_length):
            if string[i] == ')':
                total_open_bracket -= 1
            if total_open_bracket == 0:
                return i
            if string[i] == '(':
                total_open_bracket += 1

    def solve(self, root, left_string, right_string):
        len_left_string = len(left_string)
        len_right_string = len(right_string)

        if len_left_string > 0:
            # Getting the starting index of the first opening bracket of the left subtree string
            starting_index = 0
            for i in range(len_left_string):
                if left_string[i] == '(':
                    break
                starting_index += 1

            left_child = TreeNode(int(left_string[0:starting_index]))
            root.left = left_child
            # if starting index is greather than the total length that means,
            #  opening and closing bracket is not exists in string, so we would not traverse further
            if starting_index < len_left_string:
                # Finding the closing bracket index of first opening bracket index of the left subtree string
                closing_index = self.findClosingIndex(left_string, starting_index)
                self.solve(root.left, left_string[starting_index+1:closing_index], left_string[closing_index+2:-1:])

        if len_right_string > 0:
            # Getting the starting index of the first opening bracket of the right subtree string
            starting_index = 0
            for i in range(len_right_string):
                if right_string[i] == '(':
                    break
                starting_index += 1
            right_child = TreeNode(int(right_string[0:starting_index]))
            root.right = right_child
            # if starting index is greather than the total length that means,
            #  opening and closing bracket is not exists in string, so we would not traverse further
            if starting_index < len_right_string:
                closing_index = self.findClosingIndex(right_string, starting_index)
                self.solve(root.right, right_string[starting_index+1:closing_index], right_string[closing_index+2:-1:])
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, input_string):
        # write your code here
        # Getting the starting index of the first opening bracket
        starting_index = 0
        for i in range(len(input_string)):
            if input_string[i] == '(':
                break
            starting_index += 1
        
        # Getting the root value using the starting index of first opening bracket
        root = TreeNode(int(input_string[0:starting_index]))
        # Finding the closing bracket index of first opening bracket index
        closing_index = self.findClosingIndex(input_string, starting_index)

        # Based on the starting and closing index we would have left and right substree string
        self.solve(root, input_string[starting_index+1:closing_index], input_string[closing_index+2:-1:])
        return root
