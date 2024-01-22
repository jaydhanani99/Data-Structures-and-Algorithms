# https://www.interviewbit.com/problems/4-sum/submissions/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        # A.sort()
        # ans     =   set()
        # for i in range(len(A)):
        #     for j in range(i+1, len(A)):
        #         lo, hi = j + 1, len(A) - 1
                
        #         # O(N) Time
        #         while lo < hi:
        #             x = A[i] + A[j] + A[lo] + A[hi]
                    
        #             if x == B:
        #                 ans.add((A[i], A[j], A[lo], A[hi]))
        #                 hi -= 1
        #                 lo += 1

        #             elif x > B:
        #                 hi -= 1
        #             else:
        #                 lo += 1
        # return sorted(ans)
        
        
        res = set()
        store = dict()
        if not A or len(A)==0:
            return list(res)
        A.sort()
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                curSum = A[i]+A[j]
                if (B-curSum) in store:
                    for f, s in store[B-curSum]:
                        if i>s:
                            res.add((A[f], A[s], A[i], A[j]))
                if (curSum) not in store:
                    store[curSum] = [(i, j)]
                else:
                    store[curSum].append((i, j))
        res = list(res)
        res.sort()
        return res
        
        
        
        # Another simple approach
        dict    =   {}
        ans     =   set()
        n=len(A)
        for i in range(n):
            for j in range(i+1,n):
                for k in range (j+1,n):
                    for l in range (k+1,n):
                        if not (i==j or i==k or i==l or j==k or j==l or k==l) and (A[i]+A[j]+A[l]+A[k]) == B:
                            ans.add((A[i], A[j], A[k], A[l]))
                            # x = sorted([])
                            # if x not in ans:
                                # ans.append(x)
        return sorted(ans)
        
        