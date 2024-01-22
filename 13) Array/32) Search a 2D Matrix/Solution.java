// https://leetcode.com/problems/search-a-2d-matrix/

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // One approach could be find the specific row in which target exists by checking first and last element of that row,
        // and apply a binary search to that row.
        // Time complexity O(N + log(M))

        // Another approach: If we consider whole matrix to single array, we can say that it's entirely in sorted order
        // So some how we can apply to binary search on it. We just need to find a way to convert an array index (from 0 to N*M - 1)to 2D matrix index.
        // Time complexity O(log(N*M))

        int n = matrix.length;
        int m = matrix[0].length;

        // Applying binary search
        int low = 0;
        int high = n * m - 1;

        while (low <= high) {
            int mid = low + (high - low)/2;

            // To calculate matrix index from array index rowIndex = arrayIndex / n, and colIndex = arrayIndex % m
            int midRowIndex = mid / m;
            int midColIndex = mid % m;

            if (matrix[midRowIndex][midColIndex] == target) return true;
            else if (matrix[midRowIndex][midColIndex] < target) low = mid + 1;
            else high = mid - 1;
        }

        return false;
    }
}