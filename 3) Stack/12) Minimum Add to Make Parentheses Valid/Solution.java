// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

import java.util.*;

class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> st = new Stack<>();

        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (st.size() > 0 && st.peek() == '(' && s.charAt(i) == ')') st.pop();
            else st.push(s.charAt(i));
        }
        return st.size();
    }
}