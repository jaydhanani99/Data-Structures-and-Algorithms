# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# https://www.interviewbit.com/problems/remove-nth-node-from-list-end/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # To remove nth node from list
        # we take pointer1 and reach to the nth node
        # After reaching nth node we take pointer2 starting from the list
        # and now we increament both the pointer until pointer1 reach to the end of the list
        # When pointer1 reaches to the end we have pointer2 at last nth node
        # And we remove the pointer2th element
        
        
        
        pointer1 = head
        while pointer1 and n > 0:
            pointer1 = pointer1.next
            n -= 1
            
        # Now if we reach end of the list with pointer1 and still we have n > 0 that means list contain elements < n
        # At that time we remove the first element    
        if n > 0:
            head = head.next
            return head
        
        pointer2 = pointer2_prev = head
        while pointer1:
            pointer1 = pointer1.next
            pointer2_prev = pointer2
            pointer2 = pointer2.next
        # That means we have to remove first element
        if pointer2_prev is pointer2:
            return head.next
        # At this moment we have pointer2 at last nth element
        pointer2_prev.next = pointer2.next
        return head
        
        