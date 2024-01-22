// https://leetcode.com/problems/score-after-flipping-matrix/

class Solution {
    public int matrixScore(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        // Checking for each row, if first element of row is 0, we'll toggle, since left most bit should be 1 to make binary larger
        for (int i = 0; i < n; i++) {
            if (grid[i][0] == 0) {
                for (int j = 0; j < m; j++) {
                    grid[i][j] = grid[i][j] == 0 ? 1 : 0;
                }
            }
        }

        // Checking for each column if number of 0 is greater then toggle
        for (int j = 0; j < m; j++) {
            int zeroCount = 0;
            for (int i = 0; i < n; i++) {
                if (grid[i][j] == 0) zeroCount++;
                if (zeroCount > n/2) break;
            }

            if (zeroCount > n/2) {
                for (int i = 0; i < n; i++) {
                    grid[i][j] = grid[i][j] == 0 ? 1 : 0;
                }
            }
        }

        // After the conversion, calculating the value from binary
        int answer = 0;
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < m; j++) {
                sb.append(String.valueOf(grid[i][j]));
            }
            answer += Integer.parseInt(sb.toString(), 2);
        }

        return answer;
    }
}