// https://www.interviewbit.com/old/problems/cycle-in-undirected-graph/
// https://www.youtube.com/watch?v=UPfUFoWjk5w&t=463s&ab_channel=AnujBhaiya

public class Solution {
    // dfs would return true if cycle found
    boolean dfs (int current, ArrayList<ArrayList<Integer>> adj,boolean[] visited, int previous) {
        visited[current] = true;
        Iterator<Integer> it = adj.get(current).iterator();
        
        while(it.hasNext()) {
            int next = it.next();
            // If next vertex is already visited and it is not previously visited vertex, that means cycle exists
            if (visited[next] && next != previous) return true;
            // Else we call dfs function recursively to find cyycle
            if (!visited[next] && dfs(next, adj, visited, current)) return true;
        }
        return false;
    }
    
    ArrayList<ArrayList<Integer>> prepareGraph(int A, ArrayList<ArrayList<Integer>> B) {
        ArrayList<ArrayList<Integer>> adj  = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i <= A; i++) {
            adj.add(i, new ArrayList<Integer>());
        }
        ListIterator<ArrayList<Integer>> it = B.listIterator();
        while (it.hasNext()) {
            ArrayList<Integer> edge = it.next();
            // Adding edge for both vertex
            // so if array value is [x, y]
            // That means there is an edge from x to y vertex and y to x vertex
            adj.get(edge.get(0)).add(edge.get(1));
            adj.get(edge.get(1)).add(edge.get(0));
        }
        return adj;
    }
    
    
    public int solve(int A, ArrayList<ArrayList<Integer>> B) {
        ArrayList<ArrayList<Integer>> adj = prepareGraph(A, B);
        // // Call DFS for each vertex as there may be vertex which is not connected with each other
        // // In short one or more separate graph could also exists
        for (int i = 1; i <= A; i++) {
            boolean visited[] = new boolean[A+1];
            if (dfs(i, adj, visited, -1)) return 1;
        }
        return 0;
    }
}
