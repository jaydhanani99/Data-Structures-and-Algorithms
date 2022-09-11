# https://www.interviewbit.com/problems/remove-element-from-array/
# https://leetcode.com/problems/remove-element/submissions/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n = len(A)
        i = 0
        while i < n:
            if A[i] == B:
                del A[i]
                n -= 1
                i -= 1
            i += 1
        return n
        
        # Another approach
        #     j = 0
        #     for i in range(len(A)):
        #         if A[i] != B:
        #             A[j] = A[i]
        #             j+=1
        #     del(A[j:])
        #     return j
    
        # Another approach
        # A[:]    =   [i for i in A if i != B]
        # return len(A)
        
        
    
    # Another approach
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def removeElement(self, A, B):
    #     j = 0
    #     for i in range(len(A)):
    #         if A[i] != B:
    #             A[j] = A[i]
    #             j+=1
    #     del(A[j:])
    #     return j