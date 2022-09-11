# https://www.interviewbit.com/old/problems/find-nth-fibonacci/
# https://leetcode.com/problems/fibonacci-number/
# Reference: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

class Solution:
    def multiply(self, matrix1, matrix2):
        ### This is for 2*2 matrix only you can write generalize function ###
        # final matrix would look like [
        #                                 [x, y],
        #                                 [z, w]
        #                             ]
        
        x = matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0]
        y = matrix1[0][0]*matrix2[0][1] + matrix1[0][1]*matrix2[1][1]
        z = matrix1[1][0]*matrix2[0][0] + matrix1[1][1]*matrix2[1][0]
        w = matrix1[1][0]*matrix2[0][1] + matrix1[1][1]*matrix2[1][1]
        return [[x, y], [z, w]]
        
    
    def __init__(self):
        self.dict = {}
        
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
            
            
        if n in self.dict:
            return self.dict[n]
            
        
        if n%2 == 0:
            k = n//2
            answer = (2*self.fib(k-1) + self.fib(k))*self.fib(k)
        else:
            k = (n+1)//2
            answer = self.fib(k)*self.fib(k) + self.fib(k-1)*self.fib(k-1)
        
        # Need to check why we are getting correct answer even if we apply module in every iteration
        self.dict[n] = answer%(1000000007)
        return self.dict[n]
        
    # @param A : integer
    # @return an integer
    def solve(self, n):
        # Fastest approach with log(n) time complexity
        # Refer Method 6 https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
        return self.fib(n)
        
        
        
        
        # Another approach with O(n) we can do recursive approach too for O(logn) time complexity,
            # refer Method: 5 https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
        # As n is very large we can not use normal recursion or dynamic programming to find the fibonacci number.
        # If we n times multiply the matrix M = {{1, 1},{1, 0}} to itself,
        # (in other words calculate power(M, n )), 
        # then we get the (n+1)th Fibonacci number as the element at row and column (0, 0) 
        # in the resultant matrix.
        if n == 0:
            return 0
        
        M = [[1, 1], [1, 0]]
        # To calculate power of M^n
        # we need to find M^n
        # for the first iteration it would be M^2
        # 1,   2,   3, ...., n
        # M^2, M^3, M^4, ..., M^n+1
        # So we need to take n-1 iteration
        # Also if we do n iteration we would get n+1th number
        # However we require nth number
        # So we do n-2 iteration
        
        # n-2 iteration as last n-1 is not considered in range()
        for i in range(1, n-1):
            M = self.multiply(M, [[1, 1], [1, 0]])
        return M[0][0]%1000000007