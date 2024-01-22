// https://leetcode.com/problems/add-two-numbers/
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public void add(ListNode l1, ListNode l2, int carry) {
        int sumWithCarry = l1.val + l2.val + carry;
        if (l1.next == null && l2.next == null) {
            l1.val = (sumWithCarry)%10;
            carry = (int)((sumWithCarry)/10);
            if (carry > 0) {
                l1.next = new ListNode(carry);
            }
            return;
        }
        if (l1.next == null) {
            l1.next = new ListNode(0);
        }
        if (l2.next == null) {
            l2.next = new ListNode(0);
        }
        
        this.add(l1.next, l2.next, (int)((sumWithCarry)/10));
        l1.val = (sumWithCarry)%10;
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        add(l1, l2, 0);
        return l1;
    }
}