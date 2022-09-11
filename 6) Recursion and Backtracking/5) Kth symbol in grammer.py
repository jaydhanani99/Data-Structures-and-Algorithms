# https://leetcode.com/problems/k-th-symbol-in-grammar/


import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        
        # For n = 1 we have 1 element
        #     n = 2 we have 2 elements
        #     n = 3 we have 4 elements
        #     n = 4 we have 8 elements
        mid = math.pow(2, n-1)//2
        # Which means k lies in left half and left half is the same as (n-1)th row elements
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            # That means k is lies in right part of the array
            # Right part is the complement of the left part
            # So we return te negation of (k-mid)th element of (n-1)th row which is kth element of current row
            return int(not self.kthGrammar(n-1, k-mid))
        