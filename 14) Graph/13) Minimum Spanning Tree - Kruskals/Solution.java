// https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
// https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#
class Solution
{
    static ArrayList<ArrayList<Integer>> formatAdj(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj) {
        ArrayList<ArrayList<Integer>> edges = new ArrayList<ArrayList<Integer>>();
        HashMap<Integer, HashSet<Integer>> hm = new HashMap<>();
        for (int i = 0; i < V; i++) {
            hm.put(i, new HashSet<Integer>());
        }
        for (int i = 0; i < adj.size(); i++) {
            for (int j = 0; j < adj.get(i).size(); j++) {
                ArrayList<Integer> currentEdge = new ArrayList<Integer>();
                // Adding x, y, z in currentEdge => edge between x and y and weight z
                
                // First we check reverse edge for this edge exists or not
                if (!hm.containsKey(adj.get(i).get(j).get(0)) || !hm.get(adj.get(i).get(j).get(0)).contains(i)) {
                    hm.get(i).add(adj.get(i).get(j).get(0));
                    currentEdge.add(i);
                    currentEdge.add(adj.get(i).get(j).get(0));
                    currentEdge.add(adj.get(i).get(j).get(1));
                    edges.add(currentEdge);
                }
            }
        }
        edges.sort((l1, l2) -> l1.get(2).compareTo(l2.get(2)));
        return edges;
    }
    static int find(int parent[], int x) {
        if (parent[x] == x) return x;
        // Doing path compression here by assigning parent
        return parent[x] = find(parent, parent[x]);
    }
    static void union(int[] rank, int[] parent, int x, int y) {
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

    //Function to find sum of weights of edges of the Minimum Spanning Tree.
    static int spanningTree(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj) 
    {
        // Add your code here
        int parent[] = new int[V];
        for (int i = 0; i < V; i++) {
            parent[i] = i;
        }

        // To add only single edge in edges ArrayList
        // So undirected graph we generate add two edges x => y and y => x but here
        // in Kruskal's algo we use only single edge
        // Now we have edges in format (src_vertex, dest_vertex, weight) sorted by weight
        ArrayList<ArrayList<Integer>> edges = formatAdj(V, adj);
        
        // Now we have two function union and find
        // Union would do union of two vertex, by making both parent same.
        // To do so we use union-set by rank compression algo in union function
        // To do so we require rank array to store rank of each vertex
        int rank[] = new int[V];
        
        // According to Kruskal's Minimum Spanning Tree algorithm we take smaller edge first and check it cause cycle or not
        // If it's not cause cycle we add this edge or we discard it
        int sum = 0;
        int noOfEdges = edges.size();
        for(int i = 0; i < noOfEdges; i++) {
            int srcParent = find(parent, edges.get(i).get(0));
            int destParent = find(parent, edges.get(i).get(1));
            if (srcParent != destParent) {
                // We do union of these vertex and add it in graph
                union(rank, parent, srcParent, destParent);
                sum += edges.get(i).get(2);
            }
        }
        return sum;
    }
}