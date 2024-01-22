# https://www.interviewbit.com/old/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        output = []
        i = 0
        n = len(strings)
        first_string_length = len(strings[0])
        
        # this is to avoid the infinite loop, so we assume that our while loop would run at most first_string_length times
        while i < first_string_length:
            # Now we traverse through all the arrays starting from second array
            # and compare the ith char with all other strings
            # if match not found or i exceed with current string length we return the output
            # else we append the current char after the for loop
            for j in range(1, n):
                if i >= len(strings[j]) or strings[0][i] != strings[j][i]:
                    return ''.join(output)
            output.append(strings[0][i])
            i += 1
        return ''.join(output)
            