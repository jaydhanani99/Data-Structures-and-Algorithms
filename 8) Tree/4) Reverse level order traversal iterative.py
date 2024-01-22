# https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1

def reverseLevelOrder(root):
    # Code here
    # Here we will follow iterative approach to find the level order traversal
    # For iterative approach we will use queue to track the current root nodes
    
    # This is the same as normal level order traversal,
    # in this approach instead of pushing left child to queue first,
    # we push right child to queue as we are reversing the list at final output.
    if not root:
        return []
        
    queue = [root]
    output = [root.data]
    
    while queue:
        current_root = queue.pop(0)
        if current_root.right:
            output.append(current_root.right.data)
            queue.append(current_root.right)
            
        if current_root.left:
            output.append(current_root.left.data)
            queue.append(current_root.left)
            
    return reversed(output)