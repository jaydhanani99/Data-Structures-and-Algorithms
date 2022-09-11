// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode end = head;
        while (n > 0) {
            n--;
            end = end.next;
        }
        // Removing first element
        if (end == null) return head.next;
        
        ListNode start = head;
        while (end.next != null) {
            start = start.next;
            end = end.next;
        }
        start.next = start.next.next;
        return head;
        
    }
}