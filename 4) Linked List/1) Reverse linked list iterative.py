# https://leetcode.com/problems/reverse-linked-list/submissions/
# https://www.interviewbit.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, node: ListNode) -> ListNode:
        # Iterative approach
        if not node:
            return node

        prev = None
        current = node
        next = node.next
        while current.next is not None:
            current.next = prev
            prev = current
            current = next
            next = next.next
        current.next = prev
        return current