def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge_two_sorted_list(left, right)



def merge_two_sorted_list(left,right):
    sorted_list = []
    i=j=0
    while i < len(left) and j < len(right):
    
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
             sorted_list.append(right[j])
             j+=1
    sorted_list += left[i:]
    sorted_list += right[j:]

    return sorted_list


left = [5,8,12,56]
right = [7,9,45,51]
arr = [5,8,4,3,2,155,15,96,56,41]
print(merge_two_sorted_list(left,right))
print(merge_sort(arr))