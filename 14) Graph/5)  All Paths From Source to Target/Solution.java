// https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution {
    private List<List<Integer>> answer = new ArrayList<>();
    private List<List<Integer>> dfs(int current, int last, boolean[] visited, int[][] adj, List<Integer> current_answer) {
            // Stop traversing further when we reach last node, and add currently traversed node in answer
            if (current == last) {
                current_answer.add(last);
                answer.add(current_answer);
                return answer;
            }

            // Adding current element in current answer
            current_answer.add(current);
            int[] children = adj[current];
            for (int i = 0; i < children.length; i++) {
                dfs(children[i], last, visited, adj, new ArrayList<Integer>(current_answer));
            }
        return answer;
    }

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n = graph.length;
        boolean visited[] = new boolean[n];
        List<Integer> current_answer = new ArrayList<Integer>();
        
        dfs(0, n-1, visited, graph, current_answer);
        return answer;
    }
}