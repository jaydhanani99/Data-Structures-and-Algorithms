# https://www.youtube.com/watch?v=U81n0UYtk98&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=18
# https://practice.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1

#User function Template for python3
class Solution:
    def solve(self, output, used_one, used_zero, remaining_digit, final_output):
        if remaining_digit == 0:
            final_output.append(output)
            return
        
        # Appending "1" to current string
        self.solve(output+"1", used_one+1, used_zero, remaining_digit-1, final_output)
        
        # Appending "0" to current string only if number of "1" is greater then the number of "0"
        if used_one > used_zero:
            self.solve(output+"0", used_one, used_zero+1, remaining_digit-1, final_output)
    
    def NBitBinary(self, N):
        # code here
        
        # Given that we need to fill the digit with either 0 or 1
            # However count of 1's should be greater then the 0's
            # and string must start with 1

        #We start the string with only "1" and for every recursion step we append either "0" or "1"
        #We append "0" only if number of "1" is greater then the number of "0"
        final_output = []
        used_one = 1
        used_zero = 0
        remaining_digit = N-1

        self.solve("1", used_one, used_zero, remaining_digit, final_output)
        return final_output