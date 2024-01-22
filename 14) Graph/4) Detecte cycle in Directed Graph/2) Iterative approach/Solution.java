// https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/
// https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1/


class Solution {
    // WHITE => not visited, GREY => Being visited, BLACK => Vertex and all its descendants are visited
    static int WHITE = 0, GREY = 1, BLACK = 2;
    // Function to detect cycle in a directed graph.
    public boolean isCyclic(int A, ArrayList<ArrayList<Integer>> B) {
        // code here
        // To store the color of current vertex
        int color[] = new int[A];
        // Marking initial vertex as not visited (WHITE)
        for (int j = 0; j < A; j++) {
            color[j] = WHITE;
        }
    
        // This loop would only be useful when we have two separate graph which are not conntected with edge
        for (int i = 0; i < A; i++) {
            // If current vertex is already visited, we will continue for next iteration
            if (color[i] != WHITE) continue;
            
            Stack<Integer> st = new Stack<Integer>();
            // Pushing current vertex in stack 
            st.push(i);
    
            while (st.size() > 0) {
                // We are not poping element here, we pop element only when all it's children would be visited
                int current = st.peek();
                
                // If current vertex is not visited, we mark it as it is being visited
                if (color[current] == WHITE) {
                    color[current] = GREY;
                    
                    // Traversing adjcents of current vertex
                    Iterator<Integer> it = B.get(current).iterator();
                    while (it.hasNext()) {
                        int next = it.next();
                        // if we found next vertex that is previously being visited
                        // This means that we have back edge here, as if it does not have back edge color should be BLACK
                        // As we are marking vertex as BLACK when it's  completely visited
                        if (color[next] == GREY) return true;
                        // If next vertex is not visited yet, we push it in stack for next visit
                        if (color[next] == WHITE) st.push(next);  
                    }
                // if current vertex is not WHITE, that means either it is being visited or completed visited.
                // In both cases we can say that this vertex is completely visited, as we have pushed remaining vertex in stack
                // So remaining vertex was first visited and then only we have reached this vertex
                }else {
                    color[current] = BLACK;
                    st.pop();
                }
            }
        }
        return false;
    }
}