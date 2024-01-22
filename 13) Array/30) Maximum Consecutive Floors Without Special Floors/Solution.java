// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

import java.util.Arrays;
class Solution {
    public int maxConsecutive(int bottom, int top, int[] special) {
        Arrays.sort(special);
        int n = special.length;

        int answer = Math.max(special[0] - bottom, top - special[n-1]);

        for (int i = 1; i < special.length; i++) {
            answer = Math.max(answer, special[i] - special[i-1] - 1);
        }
        return answer;
    }
}