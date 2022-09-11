// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

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
    
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        // Sorting the edges in such a way that we have type => 3 edges first
        // So we traverse type 3 edges first and remove the remaining edges
        // So that we can remove maximum independent edges (alice's or bob's)
        Arrays.sort(edges, (a, b) -> b[0] - a[0]);
        
        // Creating parent and rank to apply Kruskal's algorithm
        int parent[] = new int[n+1];
        for(int i = 0; i < n+1; i++) {
            parent[i] = i;
        }
        int rank[] = new int[n+1];
        
        // This hashset will be used to keep track of removalble edges of type 3
        // If type 3 edges can be removed from both (alice and bob), we will remove it
        HashSet<Integer> hs = new HashSet<>();
    
        // To keep count of removable edges
        int ans = 0;
        // Maintain total visited edges to check whether we have traversed whole graph or not
        int noOfVisitedEdges = 0;
        
        // To traverse on all the edges
        int edgeLen = edges.length;
        
        // First we will traverse for edges type 1 or 3 (Traversed by Alice only)
        for(int i = 0; i < edgeLen; i++) {
            // Doing this only if edge type is 1 or 3
            int edgeType = edges[i][0];
            if (edgeType == 1 || edgeType == 3) {
                int srcParent = find(parent, edges[i][1]);
                int destParent = find(parent, edges[i][2]);
                if (srcParent != destParent) {
                    union(rank, parent, srcParent, destParent);
                    // If this edge is visited, we increase total visitedEdge count
                    noOfVisitedEdges++;
                } else {
                    // This edge can be removed (as we have detected cycle)
                    // Here we increase count only if type = 1 (Could be traversed by alice only)
                    // Else we store it in hashmap and when traverse for bob if we encounter same edge then only we remove it
                    if(edgeType == 1) {
                        ans ++;
                    }
                    if (edgeType == 3) {
                        hs.add(i);
                    }
                }   
            }
        }
        
        // If noOfVisitedEdges (For Alice) is less than n-1 (Minimum edge required to fully traverse graph)
        if (noOfVisitedEdges < n-1) return -1;
        
        // Resetting parent and rank for bob traverse
        for(int i = 0; i < n+1; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
        noOfVisitedEdges = 0;
        
        // Finding removable edges for Bob (edge type 2 or 3)
        for(int i = 0; i < edgeLen; i++) {
            // Doing this only if edge type is 2 or 3
            int edgeType = edges[i][0];
            if (edgeType == 2 || edgeType == 3) {
                int srcParent = find(parent, edges[i][1]);
                int destParent = find(parent, edges[i][2]);
            
                if (srcParent != destParent) {
                    union(rank, parent, srcParent, destParent);
                    noOfVisitedEdges++;
                } else {
                    // This edge can be removed
                    // Here we increase count only if type = 2 (Could be traversed by Bob only)
                    // Or we check this can be removed for Alice as well or not (For edge type 3)
                    if(edgeType == 2 || hs.contains(i)) { 
                        ans ++;
                    }
                }   
            }
        }
        // If noOfVisitedEdges (For Bob) is less than n-1 (Minimum edge required to fully traverse graph)
        if (noOfVisitedEdges < n-1) return -1;
        return ans;
    }
}