// https://leetcode.com/problems/longest-common-subsequence/
class Solution {
    public int find(String text1, String text2, int n, int m, int[][] dp) {
        if (n == 0 || m == 0) return 0;
        if (dp[n][m] != -1) return dp[n][m]; 
        
        // If match found we decrease n and m and call function
        if (text1.charAt(n-1) == text2.charAt(m-1)) {
            dp[n][m] = 1 + find(text1, text2, n-1, m-1, dp);
            return dp[n][m];
        }
        
        // Or we call function twice by decreamenting n and m
        dp[n][m-1] = find(text1, text2, n, m-1, dp);
        dp[n-1][m] = find(text1, text2, n-1, m, dp);
        return Math.max(dp[n][m-1], dp[n-1][m]);
        
        
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();
        int dp[][] = new int[n+1][m+1];
        for(int i = 0; i <= n; i++) {
            for(int j = 0; j <= m; j++) dp[i][j] = -1;
        }
        return find(text1, text2, n, m, dp);
    }
}