// https://leetcode.com/problems/linked-list-cycle-ii/
// https://www.interviewbit.com/problems/list-cycle/



// Definition for singly-linked list.
 class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
 }
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;
        ListNode slow = head;
        ListNode fast = head;

        // # Refer solution approach 3: Floyd's Tortoise and Hare (Cycle Detection) of https://leetcode.com/problems/find-the-duplicate-number
        // # The idea is to first find the cycle in the list
        // # we take two pointer one is slow and second is fast
        // # Initially both pointer points to the value of first element
        // # now we move slow to slow.next and fast to fast.next.next
        // # At some point both pointer would point to the same element because list have cycle
        // # Note that the intersection point is not the cycle entrance in the general case.
            
        while (slow != null && fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) break;
        }
        
        // # Now our task is to find the intersection point
        // # Now we point slow to the starting position
        // # and we traverse slow and fast by one position only
        // # When both points at the same position we would get our repetitive elements

        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;
            }
            return slow;
        }
        return null;
    }
}