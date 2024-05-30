# class Generic_Tree:
#     def __init__(self,data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)

#     def print_tree(self):
#         spaces = "   " * self.get_level()
#         prefix = spaces + '|__' if self.parent else ""
#         print(prefix + self.data)
#         for child in self.children:
#             child.print_tree()

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level+=1
#             p = p.parent
#         return level


# def build_tree():
#     root = Generic_Tree('Electronics')

#     Laptop = Generic_Tree("Laptop")
#     Laptop.add_child(Generic_Tree('Lenovo'))
#     Laptop.add_child(Generic_Tree('HP'))
#     Laptop.add_child(Generic_Tree('Mac'))

#     Cellphone = Generic_Tree("Cell_phone")
#     Cellphone.add_child(Generic_Tree('IPhone'))
#     Cellphone.add_child(Generic_Tree('Vivo'))
#     Cellphone.add_child(Generic_Tree('Oppo'))


#     Television = Generic_Tree("Television")
#     Television.add_child(Generic_Tree('Samsung'))
#     Television.add_child(Generic_Tree('LG'))

#     Other = Generic_Tree('Other')

#     Washing_machine = Generic_Tree("Washing_machine")
#     Washing_machine.add_child(Generic_Tree('Whirlpool'))
#     Washing_machine.add_child(Generic_Tree('Unido'))


#     Refregerator = Generic_Tree("Refregerator")
#     Refregerator.add_child(Generic_Tree('Haier'))
#     Refregerator.add_child(Generic_Tree('Godrej'))

#     Other.add_child(Washing_machine)
#     Other.add_child(Refregerator)




#     root.add_child(Laptop)
#     root.add_child(Cellphone)
#     root.add_child(Television)
#     root.add_child(Other)

    

#     root.print_tree()

# build_tree()



a = ['kahifmalik']

i = 3

print(a[0][i:])