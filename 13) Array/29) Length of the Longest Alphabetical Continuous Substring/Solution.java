// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution {
    public int longestContinuousSubstring(String s) {
        int current = 1;
        int answer = 1;
        int n = s.length();

        for (int i = 1; i < n; i++) {
            if ((int)s.charAt(i) == (int)s.charAt(i-1) + 1) {
                current++;
                answer = Math.max(answer, current);
            } else {
                current = 1;
            }
        }
        return answer;
    }
}