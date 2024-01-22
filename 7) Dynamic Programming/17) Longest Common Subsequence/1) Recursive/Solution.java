// https://leetcode.com/problems/longest-common-subsequence

class Solution {
    public int find(String text1, String text2, int n, int m) {
        if (n == 0 || m == 0) return 0;
        
        // If match found we decrease n and m and call function
        if (text1.charAt(n-1) == text2.charAt(m-1)) {
            return (1 + find(text1, text2, n-1, m-1));
        }
        
        // Or we call function twice by decreamenting n and m
        return Math.max(find(text1, text2, n, m-1), find(text1, text2, n-1, m));
        
        
    }
    public int longestCommonSubsequence(String text1, String text2) {
        return find(text1, text2, text1.length(), text2.length());
    }
}