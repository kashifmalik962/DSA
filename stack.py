# # stack = []
# # stack.append('https://edition.cnn.com/')
# # stack.append('https://edition.cnn.com/us')
# # stack.append('https://edition.cnn.com/us/energy-and-environment')
# # stack.append('https://edition.cnn.com/us/space-science')

# # # print(stack.pop())
# # # print(stack)
# # print(stack[-1])
# # print(stack)


# # from collections import deque
# # stack = deque()
# # # print(dir(stack))

# # stack.append('https://edition.cnn.com/')
# # stack.append('https://edition.cnn.com/us')
# # stack.append('https://edition.cnn.com/us/energy-and-environment')
# # stack.append('https://edition.cnn.com/us/space-science')
# # # print(type(stack))
# # print(stack.popleft())
# # print(stack.pop())
# # print(stack)



#                                 # CREATE A STACK CLASS


from collections import deque
class stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isempty(self):
       if len(self.container) == 0:
           return True
       else:
           return False

    def size(self):
        return len(self.container)
    
def reverse_string(s):
    for ch in s:
        ob.push(ch)

    rstr = ''
    while ob.size()!=0:
        rstr += ob.pop()
    print(rstr)

    
ob = stack()
reverse_string('we will conquere COVI-19')

# ob.push('we will conquere COVI-19')
# print(ob.reverse_stack_element())
# # print(ob.pop())
# # print(ob.peek())
# # print(ob.container)
# # print(ob.isempty())
# # print(ob.size())



# print("('"kashif"')")
# print("((((10+20))))")