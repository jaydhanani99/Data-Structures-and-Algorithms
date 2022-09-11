# https://www.youtube.com/watch?v=eyCj_u3PoJE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=17
# https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
        
    def solve(self, current_output, remaining_open, remaining_close, output):
        # if remaining_open == 0 that means we have used all the open brackets so we append remaining close bracket and add it to output
        if remaining_open == 0:
            output.append(current_output+(')'*remaining_close))
            return
        
        # Now we have two options either we can put open bracket or close bracket
        # However we can only put close bracket if open bracket is greater than the close bracket
        # Which means remaining open bracket is less than the remaining close bracket
        if remaining_open < remaining_close:
            # Adding close bracket and decreasing remaining_close bracket count by 1
            self.solve(current_output+")", remaining_open, remaining_close-1, output)
        # Also we can put the open bracket
        # Adding open bracket and decreasing remaining_open bracket count by 1
        self.solve(current_output+"(", remaining_open-1, remaining_close, output)
        
        
    def generateParenthesis(self, n):
        if n == 0:
            return []
        
        output = []
        # To solve this problem at every recursion step we have two options either use open bracked or use close bracket
        # However we cannot use close bracket at starting position
        # Also we cannot use open or close breacked greater than n
        # So for every recursion step we need to maintain the count of remaining open and closed brackets
        
        # Initially we have put open bracket and decreased the count of remaining open bracket by 1
        self.solve("(", n-1, n, output)
        return output