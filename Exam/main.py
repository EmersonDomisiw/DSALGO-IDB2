"""
#Descending
arr1 = [1,2,21,33,45,65,12]
for i in range(len(arr1)):
    min_idx= i
    for j in range(i+1, len(arr1)):
        if arr1[min_idx] > arr1[j]:
            arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i]
    print(arr1)
"""



"""
arr2 = [1,2,21,33,45,65,12]
print(arr2)
for i in range(len(arr2)):
    min_idx = i
    for i in range(i + 1, len(arr2)):
        if arr2[min_idx] > arr2[i]:
            arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
    print(arr2)
"""

""
#Ascending
arr2 = [1,2,21,33,45,65,12]
print(arr2)
for i in range(1,len(arr2)):
    key = arr2[i]
    j = i-1
    while j >= 0 and key < arr2[j]:
        arr2[j+1] = arr2[j]
        j-=1
        arr2[j+1] = key
print("Ascending:")
print(arr2)
""
