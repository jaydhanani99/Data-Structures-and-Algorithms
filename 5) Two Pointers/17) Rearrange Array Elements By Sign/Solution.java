// https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution {
    public int[] rearrangeArray(int[] nums) {
        int positive = 0, negative = 1;
        int[] output = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                output[positive] = nums[i];
                positive += 2;
            }
            else {
                output[negative] = nums[i];
                negative += 2;
            }
        }
        return output;
    }
}