// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

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

    public ListNode reverseList(ListNode head) {
        ListNode node = head;
        ListNode prev = null;
        ListNode current = node;
        ListNode next = node.next;
        while (current.next != null){
            current.next = prev;
            prev = current;
            current = next;
            next = next.next;
        }
        current.next = prev;
        return current;
    }

    public int pairSum(ListNode head) {
        int ans = 0;
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // Now slow is pointing to mid element of linkedlist
        // Let's reverse the right part of the list
        ListNode rightReversed = reverseList(slow);

        while (rightReversed != null) {
            ans = Math.max(ans, head.val + rightReversed.val);
            head = head.next;
            rightReversed = rightReversed.next;
        }
        return ans;
    }
}