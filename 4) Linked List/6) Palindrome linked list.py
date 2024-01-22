# https://leetcode.com/problems/palindrome-linked-list/
# https://www.interviewbit.com/problems/palindrome-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # First we find the mid point  of list
        # After finding mid point of list we reverse the right part of list
        # After reversing right part we compare the left part with the right part of the list
        
        # To find the mid point of list
        # We take two pointer first is slow and second is fast
        # slow pointer will point to next node and fast pointer will point to next of next node
        # When we reach end of the list of fast pointer our slow pointer will be point to mid of the list
        
        slow = head
        fast = head
        
        # For the even number of element slow pointer will point to first mid element
        # For the odd number of element slow pointer will point to mid of the list
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        # Reversing the right part of the list
        # fast will be None in the case of 1,2 at that time we do not required to next slow
        if fast is not None:
            slow = slow.next
        
        prev = None
        
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        # now we have prev as head of second list
        pointer1 = head
        pointer2 = prev
        
        while pointer1 and pointer2:
            if pointer1.val != pointer2.val:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return True
            
        
        
            