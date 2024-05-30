# class Binary_search_tree:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_child(self,data):
#         if self.data == data:
#             return # node already exist
        
#         if data < self.data:
#             if self.left:
#                 # Insert into left subtree
#                 self.left.add_child(data)
#             else:
#                 self.left = Binary_search_tree(data)

#         else:
#             if self.right:
#                 # Insert into right subtree
#                 self.right.add_child(data)
#             else:
#                 self.right = Binary_search_tree(data)


#     def search(self,val):
#         if self.data == val:
#             return val
        
#         if val < self.data:
#             if self.left:
#                 return self.left.search(val)
#             else:
#                 return False

#         if val > self.data:
#             if self.right:
#                 return self.right.search(val)
#             else:
#                 return False
    
#     def find_min_ele(self):
#         if self.left is None:
#             return self.data
#         else:
#             return self.right.find_min_ele()


#     def find_max_ele(self):
#         if self.right is None:
#             return self.data
#         else:
#             return self.right.find_max_ele()
        

#     def find_sum_all_ele(self):
#         values = []
#         if self.left:
#             values += self.left.in_order_traversal()
#         values.append(self.data)
#         if self.right:
#             values += self.right.in_order_traversal()
#         return sum(values)


#     def in_order_traversal(self):
#         element = []
#         # Visit left subtree
#         if self.left:
#             element += self.left.in_order_traversal()
#         element.append(self.data)
#         # Visit right subtree
#         if self.right:
#             element += self.right.in_order_traversal()

#         return element
    
#     def delete(self,val):
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)

#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)

#         else:
#             if self.left is None and self.right is None:
#                 return None
            
#             if self.left is None:
#                 return self.right
#             if self.right is None:
#                 return self.left
            
#             min_val = self.right.find_min_ele()
#             self.data = min_val 
#             self.right = self.right.delete(min_val)
#         return self

# def build_tree(element):
#     root = Binary_search_tree(element[0])
#     for i in range(1,len(element)):
#         root.add_child(element[i])
#     print(root.in_order_traversal())
    
# element = [2,17,6,19,56,45,27,12]
# build_tree(element)
















class Binary_search_tree:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

    def add_child(self,child):
        if child == self.data:
            return # if node is already exist
        
        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = Binary_search_tree(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = Binary_search_tree(child)
        
    def in_order_traversal(self):
        element = []

        if self.left:
            left_elements = self.left.in_order_traversal()
            element+=left_elements
        element.append(self.data)
        if self.right:
            right_elements = self.right.in_order_traversal()
            element+=right_elements
        return element


def build_tree(ele):
    bst = Binary_search_tree(ele[0])
    for i in range(1,len(ele)):
        bst.add_child(ele[i])

    print(bst.in_order_traversal())

build_tree([0,12,14,15,20,23,27,88])
