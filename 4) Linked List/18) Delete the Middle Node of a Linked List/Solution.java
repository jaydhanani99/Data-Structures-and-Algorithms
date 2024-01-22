// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
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
    public void delete(ListNode slow, ListNode fast) {
        if (fast == null || fast.next == null) {
            slow.next = slow.next.next;
            return;
        }
        delete(slow.next, fast.next.next);
    }
    public ListNode deleteMiddle(ListNode head) {
        if (head == null || head.next == null) return null;
        delete(head, head.next.next);
        return head;
    }
}