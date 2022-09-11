# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Here we just need to create two separate linked list
        #     1) Which contains node less then x
        #     2) Which contains node greater then or equal to x
        
        # So we will have list1 and list2
        # Initially we take list1 and it's head as None
        list1_head = ListNode(0)
        list1 = list1_head
        
        # Initially we take list2 and it's head as None
        list2_head = ListNode(0)
        list2 = list2_head
        # We have list1_head and list2_head is dummy node which is useful to find actual head of both the list
            # using list1_head.next and list2_head.next
        
        # Upon assing new nodes to list1 and list2 we change the pointer list1 and list2 
        # whereas we do not change list1_head and list2_head which will be useful to connect both the list
        
        # Traversing input list
        while head:
            # If current node value of given list is less then x we store it to list1
            if head.val < x:
                list1.next = head
                list1 = list1.next
            # else we store it to list2
            else:
                list2.next = head
                list2 = list2.next
                
            head = head.next
        # Now we connect list1 with list2
        list1.next = list2_head.next
        
        # After connecting two separate list we update list1_head which is the list1_head.next
        list1_head = list1_head.next
        
        # At last we set list2.next = None which is the end of final list
        list2.next = None
        
        # Returning actual head of list1
        return list1_head
                    
            