# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = pointer = ListNode(0)
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                pointer.next = head
                pointer = pointer.next
            head = head.next
        # For ex [1, 2, 2] we need to set pointer.next to None bcz it was pointing to last non repeating element
        pointer.next = None
                
        return new_head.next
                    