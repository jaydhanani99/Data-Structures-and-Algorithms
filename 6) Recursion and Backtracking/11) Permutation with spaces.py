# https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1
# https://www.youtube.com/watch?v=1cspuQ6qHW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=14

class Solution:
    def solve(self, input, output, final_output):
        if len(input) == 0:
            final_output.append(output)
            return
            
        # Include space in output
        self.solve(input[1::], output+" "+input[0], final_output)
        #Include without space in output
        self.solve(input[1::], output+input[0], final_output)
        return
        
    def permutation (self, S):
        # code here
        input = S
        
        # Include first char in output as there is no space before the first char
        output = S[0]
        
        # Create recursive tree with either include space or not include space for better understanding
        
        final_output = []
        
        # We are not going to include first char in input as we have already stored in output
        self.solve(input[1::], output, final_output)
        
        return final_output