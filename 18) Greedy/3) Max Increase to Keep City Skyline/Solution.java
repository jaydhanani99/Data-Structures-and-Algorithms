// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        // The simple solution would be take the maximum of next elements of current row and column and new value would be minimum of it

        int n = grid.length;
        int answer = 0;
        int[] rowMaxes = new int[n];
        int[] colMaxes = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rowMaxes[i] = Math.max(rowMaxes[i], grid[i][j]);
                colMaxes[j] = Math.max(colMaxes[j], grid[i][j]);
            }
        }


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer += Math.min(rowMaxes[i], colMaxes[j]) - grid[i][j];
            }
        }
        return answer;
    }
}