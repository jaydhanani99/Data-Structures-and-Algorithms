# https://www.interviewbit.com/old/problems/add-binary-strings/
# https://leetcode.com/problems/add-binary


class Solution:
    def addBinary(self, string1: str, string2: str) -> str:
        n1 = len(string1)
        n2 = len(string2)
        carry = 0
        output = []
        
        # Appending extra 0 to lower length of string
        if n1 > n2:
            string2 = '0'*(n1-n2)+string2
        if n2 > n1:
            string1 = '0'*(n2-n1)+string1
        
        i = max(n1, n2)-1
        
        # Start adding each digit one by one starting from LSB
        while i >= 0:
            output_num = int(string1[i])+int(string2[i])+carry
            output.append(str(output_num%2))
            carry = 0 if output_num < 2 else 1
            i -= 1
        
        
        if carry == 1:
            output.append('1')
        return ''.join(reversed(output))