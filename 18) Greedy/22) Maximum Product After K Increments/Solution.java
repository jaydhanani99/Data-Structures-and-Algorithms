// https://leetcode.com/problems/maximum-product-after-k-increments/

import java.util.*;
class Solution {
    public int maximumProduct(int[] nums, int k) {
        if (nums.length == 1) {
            long answer = (nums[0]+k)%1000000007;
            return (int)answer;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < nums.length; i++) {
            pq.offer(nums[i]);
        }

        while (k > 0) {
            // Insted of adding 1 every time we can add minimum of (difference between min1 and min2, k) directly
            // e.g. k = 4, input = [1, 17, 18]. min1 = 1 and min2 = 17, so we can directly add 4 to 1.
            int min1 = pq.poll();
            int min2 = pq.poll();
            int maxAdd = Math.min(k, (min2-min1)+1); // In case of 17 and 18, we can directly add 2 to 17. In case of 17 and 17 we need to add 1. so min2-min1+1
            min1 += maxAdd;
            k -= maxAdd;
            pq.offer(min1);
            pq.offer(min2);
        }
        long answer = 1;
        while (pq.size() > 0) {
            int current = pq.remove();
            answer = (answer*current)%1000000007;
        }
        return (int)(answer);
    }
}