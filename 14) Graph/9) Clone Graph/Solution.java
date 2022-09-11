// https://leetcode.com/problems/clone-graph/
// https://www.interviewbit.com/problems/clone-graph/


class Solution {
    
    private void dfs(Node currentNode, Node currentNewNode, HashMap<Integer, Node> visited) {
        if (visited.containsKey(currentNode.val)) return;
        
        // Adding current graph key and Node in visited HashMap
        visited.put(currentNode.val, currentNewNode);

        Iterator<Node> it = currentNode.neighbors.iterator();

        while(it.hasNext()) {
            Node next = it.next();
            Node nextNew;
            // If next Node is already exists in visited, then instead of creating new taking from visited array
            if (visited.containsKey(next.val)) {
                nextNew = visited.get(next.val);
            } else {
                nextNew = new Node(next.val);  
            }
    
            currentNewNode.neighbors.add(nextNew);
            dfs(next, nextNew, visited);
        }
        
    }
    
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        
        // To keep track of visited node and it's new Node object
        HashMap<Integer, Node> visited = new HashMap<Integer, Node>();
        Node newNode = new Node(node.val);
        
        dfs(node, newNode, visited);
        return newNode;
    }
}