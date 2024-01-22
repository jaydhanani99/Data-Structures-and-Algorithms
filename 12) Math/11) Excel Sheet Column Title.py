# https://www.interviewbit.com/problems/excel-column-title/
# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, n: int) -> str:
        output = []
        
        while n > 26:
            reminder = n%26
            if reminder == 0:
                reminder = 26
                n -= 1
            output.append(chr(reminder+64))
            n //= 26
        output.append(chr(n+64))
        
        return ''.join(reversed(output))