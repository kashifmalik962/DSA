# wlmrt_stock_price = []
# wlmrt_stock_price.insert(0,121)
# wlmrt_stock_price.insert(0,123.12)
# wlmrt_stock_price.insert(0,124.34)
# print(wlmrt_stock_price.pop())
# print(wlmrt_stock_price)



# from collections import deque

# q = deque()
# q.appendleft(121.11)
# q.appendleft(122.05)
# q.appendleft(123.91)
# q.appendleft(119.55)
# print(q)
# print(q.pop())
# print(q.pop())



# from collections import deque

# class Queue:
#     def __init__(self):
#         self.wlmrt_stock_price = deque()

#     def enqueue(self,val):
#         self.wlmrt_stock_price.appendleft(val)


#     def dequeue(self):
#         return self.wlmrt_stock_price.pop()
    
#     def isempty(self):
#         return len(self.wlmrt_stock_price) == 0
    
#     def size(self):
#         return len(self.wlmrt_stock_price)
    

    
# ob = Queue()
# ob.enqueue({'company':'Wall mart',
#            'timestamp': '15 apr, 11.01 AM',
#            'price':131.10
#             })
# ob.enqueue({'company':'Wall mart',
#            'timestamp': '15 apr, 11.02 AM',
#            'price':132
#             })
# ob.enqueue({'company':'Wall mart',
#            'timestamp': '15 apr, 11.03 AM',
#            'price':135
#             })

# print(ob.wlmrt_stock_price)
# print(ob.dequeue())
# print(ob.dequeue())





# from collections import deque
# import time

# class queue:
#     def __init__(self):
#         self.q = deque()

#     def order(self,ord):
#         for i in ord:
#             print('Placing order for :',i)
#             time.sleep(0.5)
#             self.q.appendleft(i)
    

#     def serve_order(self):
#         print("Serving Order...")
#         while self.q:
#             if self.q!=None:
#                 time.sleep(2)
#                 print('serving order :',self.q.pop())
#                 time.sleep(1)


# ob = queue()
# ob.order(['pizza','samosa','pasta','biryani','burger','tea'])
# ob.serve_order()






