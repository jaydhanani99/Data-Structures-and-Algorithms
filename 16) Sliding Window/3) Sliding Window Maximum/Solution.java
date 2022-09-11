// https://leetcode.com/problems/sliding-window-maximum/


class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        
        int[] ans = new int[n-k+1];
        
        ArrayDeque<Integer> de = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            // Removing smaller elements from last in queue
            while (!de.isEmpty() && de.peekLast() < nums[i]) de.pollLast();
            
            // Adding current element in queue
            de.offer(nums[i]);
            if (i >= k-1) {
                ans[i-k+1] = de.peekFirst();
                // Removing first element of current window if it exists in queue's first element
                if (nums[i-k+1] == de.peekFirst()){
                    de.pollFirst();
                }
            }
        }
        return ans;
    }
}