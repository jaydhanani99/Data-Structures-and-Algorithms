// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

import java.util.*;

class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);

        int i = 0, j = nums.length - 1;
        int answer = Integer.MIN_VALUE;
        while (i < j) {
            answer = Math.max(answer, nums[i] + nums[j]);
            i++;j--;
        }
        return answer;
    }
}