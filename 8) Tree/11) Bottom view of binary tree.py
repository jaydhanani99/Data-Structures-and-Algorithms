# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

def bottomView(root):
    if not root:
            return root
            
    # for the root horizontal level is 0 and for left child it would be decreamented by 1
    # and for the right child it would be increamented by 1
    root.horizontal_level = 0
    
    queue = [root]
    level_dict = {}
    
    # We do level order traversal and store horizontal level wise values,
    # This is the same approach as we have done in top view
    # However instead of checking we have already visited this horizontal level or not
    # we will replace the value if we encountered the horizontal level again
    # So that bottom view would be overwritten to the top view
    while queue:
        root = queue.pop(0)
        # Storing horizontal level of current node
        level_dict[root.horizontal_level] = root.data
        
        if root.left:
            # Decreamenting horizontal level for left child
            root.left.horizontal_level = root.horizontal_level - 1
            queue.append(root.left)
        
        if root.right:
            # Increamenting horizontal level for right child
            root.right.horizontal_level = root.horizontal_level + 1
            queue.append(root.right)
    output = []
    for i in sorted (level_dict.keys()) :
        output.append(level_dict[i])
    return output