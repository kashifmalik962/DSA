class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.children.append(child)


    def print_tree(self):
        spaces = '  ' * self.get_level()
        print(spaces + self.data)
        for child in self.children:
            child.print_tree()

   
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level


def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptops')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))


    cellphone = TreeNode('Cell phone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Google Pixel'))
    cellphone.add_child(TreeNode('Vivo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))


    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
   
    root.print_tree()

build_product_tree()








                                    # EXERCISE


# class TreeNode:
#     def __init__(self,data,designation):
#         self.data = data
#         self.designation = designation
#         self.children = []
#         self.parent = None

#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)

#     def print_tree(self):
#         spaces = '  ' * self.get_level()
#         prefix = spaces+'|_ _' if self.parent else ""
#         print(prefix+self.data)
#         for child in self.children:
#             child.print_tree()

    
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level+=1
#             p = p.parent
#         return level
        

# def build_management_tree():

#     ceo = TreeNode("Nilupul", "CEO")


#     infra_head = TreeNode("Vishwa","Infrastructure Head")
#     infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
#     infra_head.add_child(TreeNode("Abhijit", "App Manager"))

#     cto = TreeNode("Chinmay", "CTO")
#     cto.add_child(infra_head)
#     cto.add_child(TreeNode("Aamir", "Application Head"))

#     # HR hierarchy
#     hr_head = TreeNode("Gels","HR Head")

#     hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
#     hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

#     ceo.add_child(cto)
#     ceo.add_child(hr_head)
    
#     ceo.print_tree()

# build_management_tree()







