# def Selection_sort(arr):
#     size = len(arr)
#     for i in range(size-1):
#         min_index = i
#         for j in range(min_index+1,size):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         if i != min_index:
#             arr[i],arr[min_index] = arr[min_index],arr[i]
#     return arr

# print(Selection_sort(arr=[5,4,2,8,9,7,3,1]))








                                 # EXERCISE


def Selection_sort(arr):
    size = len(arr)
    print(type(arr))
    for i in range(size):
        min_index = i
        for j in range(min_index+1,size):
            if list(j.values())[0] > list(min_index.values())[i]:
                min_index = j

        # if i != min_index:
        #     arr[i],arr[min_index] = arr[min_index],arr[i]
        #     print(list(arr[v].values())[0])
            break

Selection_sort(arr=[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
])