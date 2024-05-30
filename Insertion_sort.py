def Insertion_sort(elements):
    count = 0
    
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            count+=1
            elements[j+1] = elements[j]
            j = j-1
            elements[j+1] = anchor
    return elements,count

print(Insertion_sort(elements=[11,9,29,7,2,15,28]))











#                                    # EXERCISE


# # def Insertion_sort(elements):
# #     avg = 0
# #     c = 0
# #     for i in range(1,len(elements)):
# #             c+=elements[i-1]
# #             avg = c/elements[i-1]
# #             print(avg)
# #     return avg

# # print(Insertion_sort(elements=[11,9,29,7,2,15,28]))











# def insertion_sort(elements):
#     size = len(elements)
#     count = 0

#     for i in range(1,size):
#         for j in range(i):
#             if elements[i] < elements[j]:
#                 print(elements[i],elements[j])
#                 tem = elements[i]
#                 elements[j] = elements[i]
#                 elements[i] = tem

#     return elements

# print(insertion_sort([5,4,3,2,1]))