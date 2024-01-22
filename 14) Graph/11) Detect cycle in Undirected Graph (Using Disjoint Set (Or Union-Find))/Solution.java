// https://www.geeksforgeeks.org/union-find/
// https://www.interviewbit.com/problems/cycle-in-undirected-graph/

public class Solution {

    // Recursively find the parent of vertex which returns the subset of vertex
    int find(int parent[], int vertex) {
        if (parent[vertex] == -1) {
            return vertex;
        }
        return find(parent, parent[vertex]);
    }
    
    void union(int parent[], int source, int dest) {
        parent[source] = dest;
    }
    
    
    public int solve(int A, ArrayList<ArrayList<Integer>> B) {
        // Detect cycle using union find algorithm
        // To store the parent of vertex
        
        int parent[] = new int[A+1];
        // Initially parent of all vertices would be -1
        for(int i = 0; i < A+1; i++) {
            parent[i] = -1;
        }

        ListIterator<ArrayList<Integer>> it = B.listIterator();
        while (it.hasNext()) {
            ArrayList<Integer> edge = it.next();
            // Finding parent for both vertex
            // so if array value is [x, y]
            // That means there is an edge from x to y vertex and y to x vertex
            int srcParent = find(parent, edge.get(0));
            int destParent = find(parent, edge.get(1));
            // If both parent is same that means cycle is present
            if (srcParent == destParent) return 1;
            union(parent, srcParent, destParent);
        }
        return 0;
    }
}
