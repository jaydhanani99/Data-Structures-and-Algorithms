# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pointer = head
        
        while pointer:
            pointer2 = pointer
            # We start from current pointer and traverse until we find the next value is not same as current
            while pointer2.next and pointer2.val == pointer2.next.val:
                pointer2 = pointer2.next
            # After that we have pointer2 at last occurance of same element so we link our pointer with pointer2.next
            pointer.next = pointer2.next
            pointer = pointer.next
        return head