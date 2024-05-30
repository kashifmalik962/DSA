# import time
# import numpy as np


# start = time.time()
# def bubble_sort(elements):
#     count = 0 
#     elements = elements
#     size = len(elements)
#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             count+=1
#             if elements[j] > elements[j+1]:
#                 tem = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = tem
#                 swapped = True
    
#         if swapped==False:
#             break
#         return elements,count
    
# elements = np.random.randint(1,500,5000)
# print(bubble_sort(elements))
# print(time.time() - start)







                                    # EXERCISE

# def bubble_sort(elements):
#     elements = elements
#     size = len(elements)
#     count = 0
#     for i in range(size):
#         swapped = False
#         for j in range(size-1-i):
#             count+=1
#             if elements[j]['name'] > elements[j+1]['name']:
#                 tem = elements[j]['name']
#                 elements[j]['name'] = elements[j+1]['name']
#                 elements[j+1]['name'] = tem
#                 swapped = True
    
#         if swapped==False:
#             break
#     return elements


# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# print(bubble_sort(elements))




