class BinaryTree:
 

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None



    #Use Stack mechanism
    def preorder_iterative(self):
        pre_ordered_List = []
        
        
        stack = []
        
        stack.append(self)
        
        
        while stack:
            
            node = stack.pop()
            
            pre_ordered_List.append(node.data)
            
            
            if(node.right_child is not None):
                
                stack.append(node.right_child)
            
            if(node.left_child is not None):
            
                stack.append(node.left_child)
        








        return pre_ordered_List
    
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data