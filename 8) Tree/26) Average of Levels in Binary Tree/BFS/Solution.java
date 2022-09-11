/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        Queue<TreeNode> temp = new LinkedList<TreeNode>();
        List<Double> ans = new ArrayList<>();
        q.add(root);
        
        while (q.size() > 0) {
            // Removing current level nodes from primary queue
            double sum = 0;
            double count = 0;
            while (q.size() > 0) {
                TreeNode current = q.poll();
                sum += current.val;
                count++;
                // Adding left and right children of current level nodes to temp queue
                if (current.left != null) temp.offer(current.left);
                if (current.right != null) temp.offer(current.right);
            }
            // Assing temp queue to primary queue
            q = temp;
            // Making temp queue empty for next iteration
            temp = new LinkedList<TreeNode>();
            ans.add(sum/count);
        }
        return ans;
    }
}