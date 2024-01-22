// https://leetcode.com/problems/longest-valid-parentheses/

import java.util.*;

class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> st = new Stack<>();
        int longestLength = 0;
        int currentLength = 0;

        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (st.size() > 0 && s.charAt(st.peek()) == '(' && s.charAt(i) == ')') {
                st.pop();
                if (st.size() > 0) {
                    currentLength = i - st.peek();
                } else currentLength = i + 1; // i - 0 + 1 essentially

                longestLength = Math.max(longestLength, currentLength);
            }
            else {
                st.push(i);
            }
        }
        return longestLength;
    }
}