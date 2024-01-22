// https://www.interviewbit.com/old/problems/path-in-directed-graph/

public class Solution {
    ArrayList<ArrayList<Integer>> prepareGraph(int A, ArrayList<ArrayList<Integer>> B) {
        ArrayList<ArrayList<Integer>> adj  = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i <= A; i++) {
            adj.add(i, new ArrayList<Integer>());
        }
        ListIterator<ArrayList<Integer>> it = B.listIterator();
        while (it.hasNext()) {
            ArrayList<Integer> edge = it.next();
            // edge is ArrayList which contains two values edge[0] and edge[1]
            // Which represents the edge between edge[0] and edge[1]
            adj.get(edge.get(0)).add(edge.get(1));
        }
        return adj;
    }
    
    public int dfs(int current, int last, ArrayList<ArrayList<Integer>> adj, boolean[] visited) {
        if (current == last) {
            return 1;
        }
        
        Iterator<Integer> it = adj.get(current).iterator();
        // Marking current vertex as visited
        visited[current] = true;
        while (it.hasNext()) {
            int next = it.next();
            if (!visited[next] && dfs(next, last, adj, visited) == 1) return 1;
        }
        
        return 0;
    }
    
    public int solve(int A, ArrayList<ArrayList<Integer>> B) {
        ArrayList<ArrayList<Integer>> adj = prepareGraph(A, B);
        boolean visited[] = new boolean[A+1];
        return dfs(1, A, adj, visited);
    }
}