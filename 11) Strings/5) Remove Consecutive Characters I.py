# https://www.interviewbit.com/old/problems/remove-consecutive-characters/

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, string, B):
        n = len(string)
        i = 0
        output = []
        
        while i < n:
            start = i
            while i+1 < n and string[i] == string[i+1]:
                i += 1
            # That means total number of repeating elements is equals to the given B
            if start+B != i+1:
                output.append(string[start:i+1])
            i += 1
        return ''.join(output)
        