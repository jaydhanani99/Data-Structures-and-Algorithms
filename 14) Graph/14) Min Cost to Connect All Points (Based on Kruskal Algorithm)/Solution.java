// https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution {
    PriorityQueue<int[]> prepareEdges(int[][] points) {
        PriorityQueue<int[]> edges = new PriorityQueue<int[]>((a,b)->a[2]-b[2]);
        int n = points.length;
        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                ArrayList<Integer> currentEdge = new ArrayList<Integer>();
                // Considering edge between i and j
                // Adding weight for the edge between point (points[i] and points[j])
                edges.add(new int[]{ i, j, Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]) });
            }
        }
        return edges;
    }
    
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

    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        // So consider we have total n vertices
        // Let's first create all possible edges
        PriorityQueue<int[]> edges = prepareEdges(points);
        // Here we use Kruskal's algorithm to check cycle exists or not (minimum edges required to join all the points)

        int parent[] = new int[n];
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        int rank[] = new int[n];
        
        int edgeLen = edges.size();
        int ans = 0;

        for(int i = 0; i < edgeLen; i++) {
            int[] edge = edges.poll();
            int srcParent = find(parent, edge[0]);
            int destParent = find(parent, edge[1]);
            
            if (srcParent != destParent) {
                union(rank, parent, srcParent, destParent);
                ans += edge[2];
            }
        }

        return ans;
    }
}