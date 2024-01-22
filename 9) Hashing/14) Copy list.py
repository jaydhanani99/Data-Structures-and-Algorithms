# https://leetcode.com/problems/copy-list-with-random-pointer/submissions/
# https://www.interviewbit.com/old/problems/copy-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # Which would keep the mapping of the node address: array index (where it was stored)
        dict = {}
        # To add every node of linked list index wise
        array = []
        # To add every node of new linked list index wise
        new_array = []
        
        index = 0
        while head:
            # Adding mapping of node and index in dict
            dict[head] = index
            # Appending current head in array
            array.append(head)

            # Appending new node for new linked list in new array
            new_array.append(Node(head.val))
            
            index += 1
            head = head.next
        
        # Now we traverse through array and set the next and random pointer of the new linked list based on array and dict with the help of new_array
        n = len(array)
        for i in range(n):
            if array[i].next:
                new_array[i].next = new_array[dict[array[i].next]]
            
            if array[i].random:
                new_array[i].random = new_array[dict[array[i].random]]
        return new_array[0]