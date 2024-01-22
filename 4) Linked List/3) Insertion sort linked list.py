# https://www.interviewbit.com/problems/insertion-sort-list/
# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        current = head
        
        while current:
            pointer = current.next
            # comparing current elements with all next elements of list
            while pointer:
                # if current element is greater then the next element, swap the value
                if pointer.val < current.val:
                    pointer.val, current.val = current.val, pointer.val
                pointer = pointer.next
            current = current.next
        return head