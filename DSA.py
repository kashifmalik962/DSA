                                    # BINARY SEARCH
import numpy
arr = numpy.sort(numpy.random.randint(1,1000,700))

n = 62
low = 0
high = len(arr) - 1
counter = 0
# print(low,high,arr,n)

while low <= high:
    counter+=1
    mid = (low+high)//2
    if arr[mid] == n:
        print(mid)
        break
    
    elif arr[mid] > n:
        high = mid - 1
    
    else:
        low = mid + 1
    
if low > high:
  print('number not available in list')



                                    # HASH TABLE

# dic = {"employe":{"kashif":{'Id':1,'salary':20000,'designation':'DS'},
#                     "Danish":{"Id":2,"salary":22000,"designation":"FSD"},
#                     "aahad":{"Id":3,"salary":180000,"designation":"DE"}}}
# print(dic['employe']['Danish']['salary'])

# print(dic.keys())



# my = {'Id':1,'salary':20000,'designation':'DS'}
# my.update({"salary": 50000})
# print(my.popitem())
# print(my)



                                    # BIG O NOTATION (N)
# com_ele = []
# cnt = 0
# cnt2 = 0
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [64,11,12,14,5,1,6,48,65]
# for i in a:
#     cnt+=1
#     for j in b:
#         cnt2+=1
#         if i == j:                                         # n^2
#             com_ele.append(i)
#         else:
#             pass

# print(com_ele)
# print(cnt+cnt2)




# list1 = [1,2,3,4,5,6,7,8,9,10,11]
# for i in list1:
#     print(id(i))


# import numpy as np

# ar = np.array([1,2,3,4,5,6,7,8,9,10])
# print(id(ar))
# print(id(ar[0]))
# print(id(ar[1]))
# print(id(ar[2]))
# print(id(ar[3]))
# print(id(ar[4]))
# print(id(ar[5]))
# print(id(ar[6]))
# print(id(ar[7]))
# print(ar)
 
# ar = [1,2,3,4,5,6]
# print(ar)


# import sys
# integer_size = sys.getsizeof(ar[0])

# print(integer_size)

# ar = np.array([[1,2,3],[4,'5',6],[7,8,9]])
# ar[0][0]=10
# print(ar)



# l = [2200,2350,2600,2130,2190]
# # In Feb, how many dollars you spent extra compare to January
# print(abs(l[0]-l[1]))
# # Find out your total expense in first quarter (first three months) of the year
# print(l[0]+l[1]+l[2])
# # Find out if you spent exactly 2000 dollars in any month
# for index,i in enumerate(l):
#     if i == 2000:
#         print(l[index])
# else:
#     print("We can't' spent exactly 2000 dollars in any month")

# # June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

# l.insert(5,1980)
# print(l)

# l[3] = 2130-200
# print(l)



# # Length of the list
# heros=['spider man','thor','hulk','iron man','captain america']
# print(len(heros))

# # Add 'black panther' at the end of this list
# heros.append('black panther')
# print(heros)

# # You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'

# heros.pop()
# print(heros)

# heros.insert(3,'Black panther')
# print(heros)

# # Now you don't like thor and hulk because they get angry easily :)
# # So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# # Do that with one line of code

# heros[1:3] = ['Doctor strange']
# print(heros)

# # Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# heros.sort()
# print(heros)


# def odd(n):
#     for i in range(1,n):
#         # print(i)
#         if i%2!=0:
#             print(i)

# n = int(input('Enter a maximum number :'))

# odd(n)





