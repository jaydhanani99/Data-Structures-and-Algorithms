# https://www.youtube.com/watch?v=4eOPYDOiwFo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=16
# https://leetcode.com/problems/letter-case-permutation/submissions/

class Solution:
    def __init__(self):
        self.ans = []
    def solve(self, n, output):
        if n == 0:
            self.ans.append(output)
            return

        # Include output as it is without using upper case
        self.solve(n-1, output)

    
        # Include output with current char as upper case only if it is non numeric
        if not output[n-1].isnumeric():
            output_list = list(output)
            output_list[n-1] = output_list[n-1].upper()
            self.solve(n-1, "".join(output_list))
        
    def letterCasePermutation(self, s):
        # code here
        n = len(s)
        
        # Same problem as Permutation with case change if we encounter integer we simply add without case modification
        # Initially we will take input string as output
        output = s.lower()
        
        self.solve(n, output)
        
        return self.ans