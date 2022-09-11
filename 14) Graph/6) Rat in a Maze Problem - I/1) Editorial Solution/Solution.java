// https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
// https://www.geeksforgeeks.org/rat-in-a-maze-problem-when-movement-in-all-possible-directions-is-allowed/

// m is the given matrix and n is the order of matrix
class Solution {
    
    private static ArrayList<String> answer;
    private static boolean[][] getCopy(boolean[][] visited, int n) {
        boolean[][] visitedCopy = new boolean[n][];
        for (int i = 0; i < n; i++) {
            visitedCopy[i] = visited[i].clone();
        }
        return visitedCopy;
    }
    
    private static void traverse(int i, int j, int[][] m, int n, String currentPath, boolean[][] visited) {

        if (i == n-1 && j == n-1) {
            answer.add(currentPath);
            return;
        }
        
        // Checking for Up
        if (i > 0 && m[i-1][j] == 1 && !visited[i-1][j]) {
            visited[i-1][j] = true;
            traverse(i-1, j, m, n, currentPath + "U", visited);
            // Mark next move as univisted to explore next possible moves
            visited[i-1][j] = false;
        }
        
        // Checking for Down
        if (i < n-1 && m[i+1][j] == 1 && !visited[i+1][j]) {
            visited[i+1][j] = true;
            traverse(i+1, j, m, n, currentPath + "D", visited);
            // Mark next move as univisted to explore next possible moves
            visited[i+1][j] = false;
        }
        
        // Checking for Left
        if (j > 0 && m[i][j-1] == 1 && !visited[i][j-1]) {
            visited[i][j-1] = true;
            traverse(i, j-1, m, n, currentPath + "L", visited);
            // Mark next move as univisted to explore next possible moves
            visited[i][j-1] = false;
        }
        
        // Checking for Right
        if (j < n-1 && m[i][j+1] == 1 && !visited[i][j+1]) {
            visited[i][j+1] = true;
            traverse(i, j+1, m, n, currentPath + "R", visited);
            // Mark next move as univisted to explore next possible moves
            visited[i][j+1] = false;
        }
        return;
    }

    public static ArrayList<String> findPath(int[][] m, int n) {
        // Your code here
        // Initialize answer and visited array
        answer = new ArrayList<String>();
        boolean visited[][] = new boolean[n][n];
        visited[0][0] = true;
        
        
        if (m[0][0] == 1) traverse(0, 0, m, n, "", visited);
        return answer;
        
    }
}