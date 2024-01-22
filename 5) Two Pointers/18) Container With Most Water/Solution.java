// https://leetcode.com/problems/container-with-most-water/

class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int answer = Integer.MIN_VALUE;

        while (left < right) {
            answer = Math.max(answer, (right - left) * Math.min(height[left], height[right]));
            if (height[left] <= height[right]) left++;
            else right--;
        }
        return answer;
    }
}