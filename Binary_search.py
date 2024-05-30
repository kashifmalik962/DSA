def linear_search(number_list,find_num):
    for index,val in enumerate(number_list):
        if val == find_num:
            return index
    return -1




def Binary_search(number_list,find_num):
    low = 0
    high = len(number_list) - 1
    counter = 0
    print(low,high,number_list,find_num)

    while low <= high:
        counter+=1
        mid = (low+high)//2
        if number_list[mid] == find_num:
            break
        
        elif number_list[mid] > find_num:
            high = mid - 1
        
        else:
            low = mid + 1
    return counter




def Binary_recursion_search(number_list,find_num,low,high):

    if high < low:
        return -1
    
    
    mid = (low+high)//2

    mid_number = number_list[mid]
    if number_list[mid] == find_num:
        return mid
    
    if mid_number < find_num:
        low = low + 1
    
    else:
        high = mid - 1
    return Binary_recursion_search(number_list,find_num,low,high)
    


number_list = sorted([8,4,66,8,9,7,5,25,98,55,66,4,8,5,1,48,56,6,85,3,78,686,35])
print(number_list)
# print(linear_search(number_list,686))
# print(Binary_search(number_list,35))
print(Binary_recursion_search(number_list,35,0,23))