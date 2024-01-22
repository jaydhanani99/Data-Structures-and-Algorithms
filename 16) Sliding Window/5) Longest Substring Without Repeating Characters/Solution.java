// https://leetcode.com/problems/longest-substring-without-repeating-characters/
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int start = 0;

        HashSet<Character> h = new HashSet<>();

        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (!h.contains(s.charAt(i))) {
                answer = Math.max(answer, i - start + 1);
            } else {
                while (s.charAt(start) != s.charAt(i)) {
                    h.remove(s.charAt(start));
                    start++;
                }
                start++;
            }
            h.add(s.charAt(i));
        }
        return answer;
    }
}