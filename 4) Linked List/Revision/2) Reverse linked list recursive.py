# https://leetcode.com/problems/reverse-linked-list/submissions/
# https://www.interviewbit.com/problems/reverse-linked-list/
# https://www.youtube.com/watch?v=KYH83T4q6Vs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    head = None
    def reverseList(self, node: ListNode) -> ListNode:
        # To handle edge case
        if not node:
            return node
        
        
        # Recursive approach
        # If current node is the last node we set last node as the head of reversed list
        if node.next is None:
            self.head = node
            # Will be useful only if there is only one element in input linked list
            return self.head
        
        # Calling function recursively
        self.reverseList(node.next)
        
        # From the second last node to first node, we do following operation
        # We change the link for current node and their next node
        next = node.next
        next.next = node  #We can also use directly node.next.next = node 

        # Which will be overwritten in next iteration except for the first node (or last node of reversed list)
        node.next = None
        
        
        # After reversing list we return the head
        return self.head