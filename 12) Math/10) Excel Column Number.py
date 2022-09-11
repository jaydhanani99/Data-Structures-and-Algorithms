# https://www.interviewbit.com/old/problems/excel-column-number/
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, columnTitle):
        count = 0
        n = len(columnTitle)
        j = 0
        # Instead of binary assume 26
        for i in range(n-1, -1, -1):
            # (26^0, 26^1, 26^2, ....)*(order of char1, order of char2, order of char3, ...)
            count += (26**(n-i-1))*(ord(columnTitle[i]) - 64)
        return count