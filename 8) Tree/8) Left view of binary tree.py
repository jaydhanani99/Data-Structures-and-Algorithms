# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

def LeftView(root):
    if not root:
            return []
            
    queue = [(root, 0)]
    output = []
    max_level = -1
    while queue:
        root, level = queue.pop(0)
        if max_level != level:
            output.append(root.data)
            max_level = level
        
        # We would add first left node as we required left view,
        # so left child would be popped first
        if root.left:
            queue.append((root.left, level+1))
            
        if root.right:
            queue.append((root.right, level+1))
                
            
    return output