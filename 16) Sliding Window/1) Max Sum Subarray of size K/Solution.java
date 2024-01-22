// https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1/

class Solution{
    static long maximumSumSubarray(int K, ArrayList<Integer> Arr,int N){
        // code here
        long ans = 0, currentSum = 0;
        // For the first window only
        for (int i = 0; i < K; i++) {
            currentSum += Arr.get(i);
        }
        ans = currentSum;
        
        // For the rest windows
        for (int i = K; i < N; i++) {
            currentSum = currentSum-Arr.get(i-K)+Arr.get(i);
            ans = Math.max(ans, currentSum);
        }
        return ans;
    }
}