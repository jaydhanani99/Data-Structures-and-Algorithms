class Solution {
    HashSet<Integer>[] prepareGraph(int n, int[][] edges) {
        HashSet<Integer>[] adj = new HashSet[n];
        for(int i = 0; i < n; i++){
            adj[i] = new HashSet<Integer>();
        }

        for(int[] edge : edges){
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }
        return adj;
    }
    
    private boolean dfs(int current, int destination, HashSet<Integer>[] adj, boolean[] visited) {
        
        if (current == destination) return true;
        if (visited[current]) return false;
        
        
        visited[current] = true;
        for(Integer next : adj[current]){
            if(dfs(next, destination, adj, visited)) return true;
        }
        
        return false;
    }
    
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        HashSet<Integer>[] adj = prepareGraph(n, edges);
        
        if(adj[source].contains(destination)){  // direct connection exists
             return true;
        }
        boolean visited[] = new boolean[n];
        return dfs(source, destination, adj, visited);
        
    }
}