<<<<<<< HEAD

=======
>>>>>>> f989260c848943d8bf58c1fc0b7527d0a488ae48
import collections
#def finder(arr1, arr2):
    
    # for i in arr1:
    #     if i in arr2:
    #         continue
    #     else:
    #         return print(f"{i} ist die fehlende Zahl.")

    #==============================================
    
<<<<<<< HEAD
"""     arr1.sort()
    arr2.sort()
=======
#     arr1.sort()
#     arr2.sort()
>>>>>>> f989260c848943d8bf58c1fc0b7527d0a488ae48
    
#     for num1, num2 in zip(arr1, arr2):
#         if num1 != num2:
#             return num1
        
#     return arr1[-1]
    




<<<<<<< HEAD
finder(arr1, arr2) """

def finder(arr1, arr2):
    
    d = collections.defaultdict(int)
    
    for num in arr2:
        d[num] += 1
        
    for num in arr1:
        if d[num] == 0:
            return num
            
        
        
    

=======
# finder(arr1, arr2)
    #==============================================

def finder(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] +=1

    for num in arr1:
        if d[num]==0:
            return num
        else:
            d[num] -=1


# Loesung: 5 ist die fehlende Zahl
>>>>>>> f989260c848943d8bf58c1fc0b7527d0a488ae48
arr1 = [1,2,3,4,5,6,7]

arr2 = [3,7,2,1,4,6]
<<<<<<< HEAD

finder(arr1, arr2)
# Loesung: 5 ist die fehlende Zahl

=======
finder(arr1, arr2)
>>>>>>> f989260c848943d8bf58c1fc0b7527d0a488ae48
