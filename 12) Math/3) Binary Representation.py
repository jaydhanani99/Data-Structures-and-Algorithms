class Solution:
	# @param A : integer
	# @return a strings
	def findDigitsInBinary(self, n):
        if n == 0:
            return 0
        binaryList  =   ""
        while n > 0:
            binaryList += str(n%2)
            n = int(n/2)
        return binaryList[::-1]



        # Another approach using Bit Manipulation
	    if n == 0:
	        return 0
	    output = []
        for i in range(32):
            if (n>>i) == 0:
                break
            if 1&(n>>i) == 1:
                output.append('1')
            else:
                output.append('0')
        return ''.join(reversed(output))