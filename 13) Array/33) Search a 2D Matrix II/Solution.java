// https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Start from top right corner. If current element is less than target move to next row else move to previous column
        int n = matrix.length;
        int m = matrix[0].length;

        int rowIndex = 0;
        int colIndex = m - 1;

        while (rowIndex < n && colIndex >= 0) {
            if (matrix[rowIndex][colIndex] == target) return true;
            else if (matrix[rowIndex][colIndex] < target) {
                rowIndex++;
            } else colIndex--;
        }
        return false;
    }
}