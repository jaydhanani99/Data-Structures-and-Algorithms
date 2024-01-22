class Solution {
    // Function to return a list containing the DFS traversal of the graph.
    public ArrayList<Integer> dfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        
        ArrayList<Integer> output = new ArrayList<Integer>();
        
        Stack<Integer> st = new Stack<Integer>();
        // As starting vertex is 0
        st.push(0);
        
        boolean visited[] = new boolean[V];
        
        while (st.size() > 0) {
            int current = st.pop();
            
            if (!visited[current]) {
                visited[current] = true;
                output.add(current);
                
                // Iterate through adjcents of current vertex in reverse order
                // To iterate in reverse order we have to use ListIterator
                // We have given that we need to print DFS from left to right, this is the reason we have to iterate in reverse order
                ListIterator<Integer> it = adj.get(current).listIterator(adj.get(current).size());
                while (it.hasPrevious()) {
                    st.push(it.previous());    
                }   
            }
        }
        return output;
    }
}