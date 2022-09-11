// https://leetcode.com/problems/split-linked-list-in-parts/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode[] answer = new ListNode[k];

        ListNode current = head;
        int n = 0;
        
        while (current != null) {
            n++;
            current = current.next;
        }
        int partitionSize = k > n ? 1 : (int)Math.ceil((n/(double)k));
        
        current = head;
        ListNode prev = head;
        
        // Adding for first partition
        int iteration = k;
        for (int i = 0; i < iteration; i++) {
            int currentPartitionSize = k > n ? 1 : (int)Math.ceil((n/(double)k));
            n = n-currentPartitionSize;
            k--;
            answer[i] = current;
            if (current == null) break;
            for (int j = 0; j < currentPartitionSize;  j++) {
                if (current == null) break;
                prev  = current;
                current = current.next;
            }
            prev.next = null;
        }
        return answer;
    }
}