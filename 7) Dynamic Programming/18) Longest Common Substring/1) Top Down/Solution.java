// https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1

class Solution{
    int longestCommonSubstr(String S1, String S2, int n, int m){
        // code here
        int matrix[][] = new int[n+1][m+1];
        int ans = 0;
        for(int i = 1; i < n+1; i++) {
            for(int j = 1; j < m+1; j++) {
                if (S1.charAt(i-1) == S2.charAt(j-1)) {
                    matrix[i][j] = 1+matrix[i-1][j-1];
                    ans = Math.max(ans, matrix[i][j]);
                }
                // When match breaks we put 0
                else matrix[i][j] = 0;
            }
        }
        return ans;
    }
}