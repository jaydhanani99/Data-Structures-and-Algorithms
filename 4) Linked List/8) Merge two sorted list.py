# Definition for singly-linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# https://www.interviewbit.com/problems/merge-two-sorted-lists/
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # We create another list and return it's head
        head = ListNode(0)
        pointer = head
        # We traverse both list and store minimum element to new list
        
        
        while l1 and l2:
            # storing minimum value of both list to new list
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
            
        # Storing remaining element if any
        while l1:
            pointer.next = l1
            l1 = l1.next
            pointer = pointer.next
        while l2:
            pointer.next = l2
            l2 = l2.next
            pointer = pointer.next
        # Returning head.next which is the actual head of new list
        return head.next