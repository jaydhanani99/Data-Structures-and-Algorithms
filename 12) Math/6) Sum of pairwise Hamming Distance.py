# https://www.interviewbit.com/old/problems/sum-of-pairwise-hamming-distance/
# https://leetcode.com/problems/total-hamming-distance

class Solution:
    # @param A : list of integers
    # @return an integer

    def cntBits(self, nums):
        # first approach is to loop over the pairs with timecomplexity O(N^2)
        # Second approach
        # Let's say we have three numbers which contain only one bit
        # e.g [1, 0, 1]
        # To count the sum we just count the number of ones which is 2 in this case and number of 0 which is 1 in this case
        # so our final ans will be 2(2)(1) = 4
        # here we have multiply with 2 becase 1,3 and 3,1 gives same value
        # Now let's say we have multiple digits number
        # so we traverse from 1st digit to 31st digit and count using the same formula
        # timecomplexity will be O(32*N) so for larger values it is  smaller then O(N^2)
        n = len(nums)
        
        count = 0
        for i in range(32):
            total_ones = 0
            # counting number of 1's
            for j in range(n):
                # comparing last digit to first digit
                if (nums[j]>>i)&1 == 1:
                    total_ones += 1
            # now we have number of 1's in count
            # so number of 0's will be len(A)-count
            count += 2*((total_ones)*(n-total_ones))%1000000007
        return count%1000000007
