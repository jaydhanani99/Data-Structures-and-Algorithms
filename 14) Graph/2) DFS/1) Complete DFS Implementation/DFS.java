import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

class Graph {
    private int v;
    private ArrayList<LinkedList<Integer>> adj;

    Graph(int v) {
        this.v = v;
        adj = new ArrayList<LinkedList<Integer>>(this.v);

        for (int i = 0; i < this.v; i++) {
            // Initializing linkedList for each vertex
            adj.add(i, new LinkedList<Integer>());
        }
    }

    void addEdge (int source, int destination) {
        // Adding edge (linkList node) for source vertex
        adj.get(source).add(destination);
    }

    void printDFS (int start) {
        boolean visited[] = new boolean[this.v];

        // Stack to traverse each vertex
        // We could also write List<Integer> st = new Stack<Integer>(); as Stack implements List
        Stack<Integer> st = new Stack<Integer>();
        st.push(start);

        while (st.size() > 0) {
            int current = st.pop();
            // Printing current element
            System.out.println(current);
            if (!visited[current]) {
                visited[current] = true;

                // Adding adjcent of current vertex in stack (This would print from right to left)
                Iterator<Integer> it = adj.get(current).iterator();
                while (it.hasNext()) {
                    st.push(it.next());
                }

                // To print from left to right, we need to iterate in reverse order
                // ListIterator<Integer> it = adj.get(current).listIterator(adj.get(current).size());
                // while (it.hasPrevious()) {
                //     st.push(it.previous());    
                // }
            }
        }
    }

    void printDFSRecursive(int current, boolean[] visited) {
        // No need to take stack as recursion works as stack
        if (!visited[current]) {
            visited[current] = true;

            System.out.println(current);

            Iterator<Integer> it = adj.get(current).iterator();
            while (it.hasNext()) {
                printDFSRecursive(it.next(), visited);
            }
        }
    }
}

public class DFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of vertices");
        int v = sc.nextInt();

        System.out.println("Enter number of edges");
        int edges = sc.nextInt();

        Graph g = new Graph(v);

        System.out.println("Enter source and destination vertex for each edge");
        for (int i = 0; i < edges; i++) {
            int source = sc.nextInt();
            int destination = sc.nextInt();

            g.addEdge(source, destination);
        }

        // ------------------------ PRINT DFS [START] --------------------------//
        // Using iterative approach
        // g.printDFS(0);

        // Using recursive approach
        boolean visited[] = new boolean[v];

        g.printDFSRecursive(0, visited);
        // ------------------------ PRINT DFS [END] --------------------------//


        sc.close();
    }
}