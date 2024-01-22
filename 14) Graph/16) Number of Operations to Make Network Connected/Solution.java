// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution {
    int find(int parent[], int x) {
        if (parent[x] == x) return x;
        // Doing path compression here by assigning parent
        return parent[x] = find(parent, parent[x]);
    }
    
     void union(int[] rank, int[] parent, int x, int y) {
        // Here in this function we do union of two vertex x and y
        // To do so first we find the parent of this two vertex and we do union of them
        // by making parent of one vertex to other
        int xParent = find(parent, x);
        int yParent = find(parent, y);

        // Here we have two options
        // 1) Make xParent to parent of yParent
        // 2) Make yParent to parent of xParent
        // Also we check rank of xParent and yParent and assign parent accordingly
        if (rank[xParent] > rank[yParent]) {
            // This condition means that xParent has larger chlidren compare to yParent
            // So we will not make child of yParent to xParent as this would cause increase in rank for yParent
            // So we will make child of xParent to yParent (or parent of yParent to xParent)
            parent[yParent] = xParent;
        } else if (rank[xParent] < rank[yParent]) {
            parent[xParent] = parent[yParent];
        } else {
            // If both have same rank we can make anyone to parent
            // Here we have made xParent -> yParent, so we have increased rank of xParent
            parent[yParent] = xParent;
            rank[xParent] += 1;
        }
    }
    
    public int makeConnected(int n, int[][] connections) {
        // n-1 edge is required to complete graph
        if (connections.length < n-1) return -1;
        
        int parent[] = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        int rank[] = new int[n];
        
        // Removable edgeCount that is causing cycle
        int edgeCount = 0;

        for (int i = 0; i < connections.length; i++) {
            int srcParent = find(parent, connections[i][0]);
            int destParent = find(parent, connections[i][1]);
            if (srcParent != destParent) {
                union(rank, parent, srcParent, destParent);
            } else {
                // It has cycle we can remove this edge
                edgeCount++;
            }
        }
        // edgeCount is the total edge that is causing cycle
        // So we can remove maximum of edgeCount edges
        // However sometimes we have some extra edges that we do not require to remove
        // To handle this scenario we have removed that extra edges from edgeCount as well
        // (this is possible when we have more than 1 cycle in graph and we have more than (n-1) total edges)
        return edgeCount - (connections.length - n + 1);
    }
}