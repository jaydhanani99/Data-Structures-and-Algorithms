// m is the given matrix and n is the order of matrix
class Solution {
    
    private static ArrayList<String> answer;
    
    private static int ix[] = {1, 0, 0, -1};
    private static int jy[] = {0, -1, 1, 0};
    private static String path = "DLRU";
    
    
    private static boolean[][] getCopy(boolean[][] visited, int n) {
        boolean[][] visitedCopy = new boolean[n][];
        for (int i = 0; i < n; i++) {
            visitedCopy[i] = visited[i].clone();
        }
        return visitedCopy;
    }
    
    private static void traverse(int i, int j, int[][] m, int n, String currentPath) {

        // System.out.println(i + "," + j + "currentPath=" + currentPath);
        if (i == n-1 && j == n-1) {
            answer.add(currentPath);
            return;
        }
        
        // We mark the visited vertex as 2 in matrix (So we do not require to maintain visited matrix)
        // Checking for all directions
        for (int k = 0; k < 4; k++) {
            // This would make path DLRU in four iteration
            int row = i + ix[k];
            int col = j + jy[k];
            if (row >= 0 && col >= 0 && row < n && col < n && m[row][col] == 1) {
                // Marking next vertex as visited
                m[row][col] = 2;
                traverse(row, col, m, n, currentPath + path.charAt(k));
                // After calling function marking next vertex as unvisited for next iteration
                m[row][col] = 1;
            }
            
        }
    }

    public static ArrayList<String> findPath(int[][] m, int n) {
        // Your code here
        // Initialize answer and visited array
        answer = new ArrayList<String>();
        
        if (m[0][0] == 1) {
            // Marking first vertex as visited
            m[0][0] = 2;
            traverse(0, 0, m, n, "");
        }
        return answer;
        
    }
}