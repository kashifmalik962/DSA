class Binary_search_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            # if subtree is exist
            if self.left:
                self.left.add_child(data)
            else:
                # Create subtree
                self.left = Binary_search_tree(data)

        else:
            if data > self.data:
                # if subtree is exist
                if self.right:
                    self.right.add_child(data)
                else:
                    # Create subtree
                    self.right = Binary_search_tree(data)


    def inorder_traversal(self):
        values = []
        if self.left:
            left_elements = self.left.inorder_traversal()
            values += left_elements
        values.append(self.data)
        if self.right:
            right_elements = self.right.inorder_traversal()
            values += right_elements
        return values


    def search(self,val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        else:
            if val > self.data:
                if self.right:
                    return self.right.search(val)
                else:
                    return False
                
    def find_min_ele(self):
        values = []
        if self.left:
            values += self.left.inorder_traversal()
        values.append(self.data)
        if self.right:
            values += self.right.inorder_traversal()
        return min(values)


    def find_max_ele(self):
        values = []
        if self.left:
            values += self.left.inorder_traversal()
        values.append(self.data)
        if self.right:
            values += self.right.inorder_traversal()
        return max(values)
    

def create_binary_tree(num):
    ob = Binary_search_tree(num[0])
    for i in range(1,len(num)):
        ob.add_child(num[i])
    print(ob.inorder_traversal())
    print(ob.find_min_ele())
    print(ob.find_max_ele())
    print(ob.search(10))
    

num = [5,10,18,20,7,3,16]

create_binary_tree(num)



