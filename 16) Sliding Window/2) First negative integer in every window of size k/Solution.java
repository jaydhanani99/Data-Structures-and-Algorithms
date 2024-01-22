// https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1/#

class Solution {
    
    public long[] printFirstNegativeInteger(long A[], int N, int K)
    {
        // Size of the output array would be N-K+1
        long ans[] = new long[N-K+1];
        // Storing negative number list in queue
        Queue<Long> dq = new LinkedList<>();
        
        
        // Traversing in each element of array
        for (int i = 0; i < N; i++) {
            // If element is negative storing in queue
            if (A[i] < 0) {
                dq.offer(A[i]);
            }
            
            // when we reach last element of first window
            if (i >= K-1) {
                // storing answer for current window
                
                // Storing 0 in case of no negative element in current window
                if (dq.size() == 0) ans[i-K+1] = 0;
                else {
                    ans[i-K+1] = dq.peek();
                    // Also removing first element of current window if it exists in queue's first element
                    if (A[i-K+1] == dq.peek()) dq.poll();
                }
            }
        }
        return ans;
    }
}