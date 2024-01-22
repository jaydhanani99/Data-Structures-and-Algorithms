
// https://www.interviewbit.com/problems/cycle-in-directed-graph/
// https://www.youtube.com/watch?v=GLxfoaZlRqs&t=11s&ab_channel=AnujBhaiya
// https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
import java.util.*;
public class Solution {

    ArrayList<ArrayList<Integer>> prepareGraph(int A, ArrayList<ArrayList<Integer>> B) {
        ArrayList<ArrayList<Integer>> adj  = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i <= A; i++) {
            adj.add(i, new ArrayList<Integer>());
        }
        ListIterator<ArrayList<Integer>> it = B.listIterator();
        while (it.hasNext()) {
            ArrayList<Integer> edge = it.next();
            // edge is ArrayList which contains two values edge[0] and edge[1]
            // Which represents the edge between edge[0] and edge[1]
            adj.get(edge.get(0)).add(edge.get(1));
        }
        return adj;
    }

    boolean dfs (int current, ArrayList<ArrayList<Integer>> adj,boolean[] visited, boolean[] rec_stack) {
        // Marking current vertex as visited
        visited[current] = true;
        // Marking current vertex as visited in this particular recursion track
        rec_stack[current] = true;
        for(Integer next: adj.get(current)) {
            if (rec_stack[next]) return true;
            if (dfs(next, adj, visited, rec_stack)) return true;
        }
        // When we complete this recursion track we mark it as unvisited
        rec_stack[current] = false;
        return false;
    }

    public int solve(int A, ArrayList<ArrayList<Integer>> B) {
        // We can detect cycle in directed graph by keeping visiting track of vertex, and if we encounter same vertex in that particular track we can say that cycle is present
        // To keep track of current vertex we use rec_stack variable which we mark as visited for each vertex, and when we complete that particular cycle (complete that paricular recursion) we mark it as unvisited so that we can use it for another vertex's track
        
        // First we call prepareGraph function to make a list of edges that belongs to particular node
        // B is the array of edges from node x to y, so we store y (more than one in case of multiple edge for same vertex) at the index of x
        ArrayList<ArrayList<Integer>> adj = prepareGraph(A, B);
        
        for (int i = 1; i <= A; i++) {
            // To keep track of visited vertex
            boolean visited[] = new boolean[A+1]; // A+1 because vertices are starting from 1
            // To maintain the visited track for vertex
            boolean rec_stack[] = new boolean[A+1];
            
            // Call DFS for each vertex as there may be vertex which is not connected with each other
            // In short one or more separate graph could also exists
            if (dfs(i, adj, visited, rec_stack)) return 1;
        }
        return 0;
    }
}