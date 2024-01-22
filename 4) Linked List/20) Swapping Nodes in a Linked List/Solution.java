// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode start = head, end = head, tempEnd = head;
        
        while (k > 1) {
            k--;
            start = start.next;
            tempEnd = tempEnd.next;
        }
        
        while (tempEnd.next != null) {
            end = end.next;
            tempEnd = tempEnd.next;
        }
        
        int temp = start.val;
        start.val = end.val;
        end.val = temp;
        
        return head;
    }
}