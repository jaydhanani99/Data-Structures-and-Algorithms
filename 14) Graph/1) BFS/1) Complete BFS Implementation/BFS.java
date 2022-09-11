import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

import javax.management.Query;

class Graph {
    private int v;
    // To store the edge from one vertex to other using linkedList
    // ArrayList would represents each vertex
    private ArrayList<LinkedList<Integer>> adj;
    
    Graph(int v) {
        this.v = v;
        adj = new ArrayList<LinkedList<Integer>>(this.v);

        // Initializing LinkedList for each vertex
        for (int i = 0; i < this.v; i++) {
            adj.add(i, new LinkedList<Integer>());
        }
    }

    void addEdge(int source, int destination) {
        // Adding link at (source) vertex, which is the root node of that linkedList and connect it with destination vertex (By adding a new node)
        adj.get(source).add(destination);
    }

    void printBFS (int start) {
        // Prining graph vertex starting from (start)
        // Default value of boolean array would be False
        boolean visited[] = new boolean[this.v];

        // We traverse each vertex starting from (start), mark it as visited and add the corresponding child in queue
        LinkedList<Integer> l = new LinkedList<Integer>();
        l.add(start);

        while (l.size() > 0) {
            // Which remove the element from last (queue)
            int current = l.poll();
            // If current vertex is not visited
            if (!visited[current]) {
                // Mark current vertex as visited
                visited[current] = true;
                System.out.println(current);

                // Iterate through all the connected vertex of current vertex
                Iterator<Integer> it = adj.get(current).iterator();
                while (it.hasNext()) {
                    // Add the connected vertex in queue, so it can be explored in next iteration
                    l.add(it.next());
                }
            }
        }
    }

    void printBFSRecursive(boolean[] visited, Queue<Integer> q) {
        // Need to take queue in recursion as well, as recursion works as stack
        if (q.isEmpty()) return;

        int current = q.poll();
        
        if (!visited[current]) {
            System.out.println(current);
            visited[current] = true;

            Iterator<Integer> it = adj.get(current).iterator();

            while (it.hasNext()) {
                q.add(it.next());
            }
        }

        printBFSRecursive(visited, q);
    }
}

public class BFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of vertices");
        int v = sc.nextInt();
        
        System.out.println("Enter number of edges");
        int edges = sc.nextInt();

        Graph g = new Graph(v);

        for (int i = 0; i < edges; i++) {
            System.out.println("Enter source and destination vertex");
            int source = sc.nextInt();
            int destination = sc.nextInt();

            // Adding edge
            g.addEdge(source, destination);
        }

        System.out.println("Enter the starting vertex");

        // ------------------------ PRINT DFS [START] --------------------------//
        // Using iterative approach
        // g.printBFS(sc.nextInt());

        // Using recursive approach
        boolean visited[] = new boolean[v];
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(sc.nextInt());
        g.printBFSRecursive(visited, q);
        // ------------------------ PRINT DFS [END] --------------------------//

        sc.close();

        
    }
}