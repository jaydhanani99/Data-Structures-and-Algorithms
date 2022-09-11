# https://www.interviewbit.com/old/problems/atoi/
# https://leetcode.com/problems/string-to-integer-atoi
import math
class Solution:
    def myAtoi(self, string: str) -> int:
        # Removing leading whitespace
        string = string.lstrip(' ')
        
        n = len(string)
        
        if n == 0:
            return 0
        
        INT_MAX = int(math.pow(2, 31)) - 1
        INT_MIN = int(INT_MAX) + 1
        
        sign = '-' 
        
        output = []
        i = 0
        # Adding - sign in output if available
        if string[0] == '-':
            output.append('-')
            i = 1
        # ignoring + sign if available
        if string[0] == '+':
            i = 1
            
        while i < n:
            # if current char is not a digit then terminate the loop
            if not string[i].isdigit():
                break
            output.append(string[i])
            i += 1
            
        output_len = len(output)
        # if empty string or string with only '-' exists then return 0
        if output_len == 0 or (output_len == 1 and output[0] == '-'):
            return 0
        
        output =  int(''.join(output))
        
        # return INT_MAX int if overflows
        if output > INT_MAX:
            return INT_MAX
        
        # return INT_MIN int if overflows
        if output < -INT_MIN:
            return -INT_MIN
        return output
        