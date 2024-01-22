// https://leetcode.com/problems/rotate-list/
// https://www.interviewbit.com/problems/rotate-list/
// https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1/#

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;

        int n = 1;
        ListNode current = head;
        ListNode last;
        // First find total length of list
        while (current.next != null) {
            n++;
            current = current.next;
        }
        // Assing last node
        last = current;
        
        // Module in case of k > n
        k = k%n;
        if (k == 0) return head;
        
        
        current = head;
        int i = n-k;
        ListNode prev = current;
        while (i > 0) {
            prev = current;
            current = current.next;
            i--;
        }
        // Now we have head, last and current (from current to last should be appended at the start of list)
        // Here current is the start of new list, and prev is end of new list and last.next will be head of old list
        last.next = head;
        prev.next = null;
        
        return current;
    }
}
