def swap(a,b,arr):
    if a!=b:
        tem = arr[a]
        arr[a] = arr[b]
        arr[b] = tem



def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]

    start = pivot_index+1
    end = len(elements) - 1
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1
            print(elements[start])

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start,end,elements)
    swap(pivot_index,end,elements)
    return end

def quick_sort(elements,start,end):
    if start < end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,pi-1)     # left partition
        quick_sort(elements,pi+1,end)       # right partition

elements = [11,9,29,7,2,15,28]
quick_sort(elements,0,len(elements)-1)
print(elements)







# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less_than_pivot = [x for x in arr[1:] if x <= pivot]
#         greater_than_pivot = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



# my_list = [3, 6, 8, 10, 1, 2, 1]
# print(quick_sort(my_list))
# Example usage:

# my_list = [[3, 6, 8, 10, 1, 2, 1],
#            [0,1,5,1,2,4,3,6,9,7,2],
#            [1,2,3,4,5,6,7,8,9],
#            [9,8,7,6,5,4,3,2,1],
#            []]
# for i in my_list:
#     sorted_list = quick_sort(i)
#     print(sorted_list)


