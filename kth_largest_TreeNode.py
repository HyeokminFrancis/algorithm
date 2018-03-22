class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    # Helper Method    
    def size(self,root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child)) 
        
    def find_kth_largest(self,root,k):
        # Return Element should be of type TreeNode
        if root is None:
            return None
        
        
        right_size = 0
        
        if root.right_child is not None:
            right_size = self.size(root.right_child)
        
        
        
        if right_size+1 == k:
            return root
            
            
            
        if right_size >= k:
            return self.find_kth_largest(root.right_child,k)
        
        else:
            return self.find_kth_largest(root.left_child,k - right_size -1) 
            
            
class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
    
    def __str__(self):
        return '%s' %self.data
   