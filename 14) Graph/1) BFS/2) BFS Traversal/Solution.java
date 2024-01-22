// https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1


class Solution {
    // Function to return Breadth First Traversal of given graph.
    public ArrayList<Integer> bfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        ArrayList<Integer> output = new ArrayList<Integer>();
        
        // To track record of visited vertices
        // Initial value of boolean would be false
        boolean visited[] = new boolean[V];
        
        // Queue to track record of BFS
        // LinkedList implements Queue (We could also initialize as LinkedList<Integer> queue...)
        Queue<Integer> queue = new LinkedList<Integer>();
        
        // Adding starting vertex in queue, here we have given that starting vertex is 0
        queue.add(0);
        
        while (queue.size() > 0) {
            // Removing last element from queue
            int current = queue.poll();
            
            // If current element is not visited
            if (!visited[current]) {
                // Marking current element as visited
                visited[current] = true;
                
                // Adding adjacent vertices of current vertex
                Iterator<Integer> it = adj.get(current).iterator();
                while(it.hasNext()) {
                    queue.add(it.next());
                }
                
                // Adding current element in output list
                output.add(current);
            }
        }
        return output;
    }
}