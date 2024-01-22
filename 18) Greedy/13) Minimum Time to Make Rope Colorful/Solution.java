// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution {
    public int minCost(String colors, int[] neededTime) {
        int n = neededTime.length;
        int answer = 0, i = 0;
        while (i < n) {
            // Idea is to sum the neededTime for every same element and at last remove the maximum neededTime among them.
            // This essentially gives the top k-1 minimum neededTime for k same colors
            int currentMax = neededTime[i];
            answer += currentMax;
            while ((i+1) < n && colors.charAt(i) == colors.charAt(i+1)) {
                currentMax = Math.max(currentMax, neededTime[i+1]);
                answer += neededTime[i+1];
                i++;
            }
            // Removing the maximum neededTime
            answer -= currentMax;
            i++;
        }

        return answer;
    }
}