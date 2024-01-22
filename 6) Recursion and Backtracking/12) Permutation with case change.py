# https://www.youtube.com/watch?v=J2Er5XceU_I&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=15
# https://www.geeksforgeeks.org/permute-string-changing-case/
# https://leetcode.com/problems/letter-case-permutation/submissions/

# If we draw the recursion tree for this problem then at every level we have two option either capitalize the current element or not
class Solution:
    def solve(self, n, output, final_output):
        if n == 0:
            final_output.append(output)
            return

        # Include output with current char as upper case
        output_list = list(output)
        output_list[n-1] = output_list[n-1].upper()
        self.solve(n-1, "".join(output_list), final_output)

        # Include output as it is without using upper case
        self.solve(n-1, output, final_output)
        return
        
    def permute (self, S):
        # code here
        n = len(S)
        
        # Initially we will take input string as output
        output = S.lower()
        
        final_output = []
        
        # n is to track the current char
        self.solve(n, output, final_output)
        
        return final_output

sol = Solution()

print(sol.permute("abc"))

