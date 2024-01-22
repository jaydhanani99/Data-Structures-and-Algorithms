// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

import java.util.*;
class Solution {
    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);

        int currentMax = nums[0], currentMin = nums[0];
        int answer = 0;
        for (int i = 0; i < nums.length; i++) {
            currentMax = Math.max(currentMax, nums[i]);
            currentMin = Math.min(currentMin, nums[i]);

            if ((currentMax - currentMin) > k) {
                answer++;
                currentMax = nums[i];
                currentMin = nums[i];
            }
        }
        if ((currentMax - currentMin) > k) {
            answer++;
        }
        return answer+1; // Considering last partition
    }
}