// https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1/

class CustomElement {
    public int current, previous;
    
    CustomElement(int current, int previous) {
        this.current = current;
        this.previous = previous;
    }
}
class Solution {
    // dfs would return true if cycle found
    boolean dfs(int start, int V, ArrayList<ArrayList<Integer>> adj) {
        boolean visited[] = new boolean[V];
        // Adding current and previous vertex in stack
        // For the undirected graph, we cannot consider the edge between two points as cycle
        // So to discard that particular edge we have to maintain the previous vertex of current vertex
        Stack<CustomElement> st = new Stack<CustomElement>();

        // For the starting vertex we consider previously visited vertex as -1
        st.push(new CustomElement(start, -1));
        
        while (st.size() > 0) {
            CustomElement c = st.pop();
    
            Iterator<Integer> it = adj.get(c.current).iterator();

            while (it.hasNext()) {
                int next = it.next();
                // if next vertex (adj of current vertex) is already visited and, 
                // which is not equal to the previously visited vertex (in short edge between two vertex) 
                if (visited[next] && next != c.previous) return true;
                
                // Adding adj vertex in stack if it is not visited
                if (!visited[next]) {
                    st.push(new CustomElement(next, c.current));
                }
            }
            
            // Marking current vertex as visited
            visited[c.current] = true;
        }
        return false;
        
    }

    // Function to detect cycle in an undirected graph.
    public boolean isCycle(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        
        // Call DFS for each vertex as there may be vertex which is not connected with each other
        // In short one or more separate graph could also exists
        for (int i = 0; i < V; i++) {
            if(dfs(i, V, adj)) return true;
        }
        
        return false;
    }
}