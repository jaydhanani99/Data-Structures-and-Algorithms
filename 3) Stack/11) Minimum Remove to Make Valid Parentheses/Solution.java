// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> st = new Stack<Integer>();
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            if (st.size() > 0 && s.charAt(st.peek()) == '(' &&  s.charAt(i) == ')') {
                st.pop();
                continue;
            }
            if (s.charAt(i) == '(' || s.charAt(i) == ')') {
                st.push(i);
            }
        }
        StringBuilder sb = new StringBuilder();
        HashSet<Integer> set = new HashSet<>(st);
        
        for (int i = 0; i < n; i++) {
            if (!set.contains(i)) {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}