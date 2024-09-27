""""
#insertion sort
arr1 = [10,2,3,1,1,4,89,21]
#printing the values

print(arr1)
for i in range(1, len(arr1)):
    key = arr1[i]
    j = i - 1
    #move element of arr1[0..i-1]
    #that are greater than the key
    #in one position ahead of
    #their current position
    while j >= 0 and key < arr1[j]:
        arr1[j + 1] = arr1[j]
        j -= 1
    arr1[j + 1] = key
print("Array after Insertion Sort:")
print(arr1)


#Selection sort
arr2 = [10,2,3,1,1,4,89,21]
print("Array 2 before Selection Sort:")
print(arr2)
for i in range(len(arr2)):
    min_idx = i
    for j in range(i + 1, len(arr2)):
        if arr2[min_idx] > arr2[j]:
            min_idx = j
    arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i] #Indention
print("Array 2 after selection sort:")
print(arr2)


#Bubble sort
arr3 = [10,2,3,1,1,4,89,21]
print("Array 3 before bubble sort:")
print(arr3)
for i in range(len(arr3)):
    for j in range(0, len(arr3) - i - 1):
        if arr3[j] > arr3[j + 1]:
           arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
print("Array 3 after bubble sort:")
print(arr3)
"""

#Activity Guide 1
#Bubble Sort: ascending
#1.[23,89, 7, 56, 44] – Implement the Bubble Sort Algorithm for the Dataset and
#sort the data into ascending order.

"""
def bubble_sort(array1):
    n = len(array1)
    for i in range(len(array1)):
        for j in range(0, len(array1) - i - 1):
            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
    print("Bubble sort in Ascending:", array1)

array1 = [23, 89, 7, 56, 44]
bubble_sort(array1)


"""
"""
#Insertion Sort: ascending
#2.[12, 78, 91, 34, 62] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into ascending
#order.

array2 =  [12, 78, 91, 34, 62]
print("Array 2 before bubble sort:")
print(array2)
for i in range(1, len(array2)):
    key = array2[i]
    j = i - 1
    while j >= 0 and key < array2[j]:
        array2[j + 1] = array2[j]
        j -= 1
    array2[j + 1] = key
print("Insertion Sort in Ascending:")
print(array2)


"""
"""
#Selection sort: descending
#3.[5, 99, 48, 15, 67] – Implement the
#Selection Sort Algorithm for the Dataset and sort the data into descending
#order.
def select_sort(array3):
    print("Array 2 before Selection Sort:")
    print(array3)
    for i in range(len(array3)):
        max_idx = i
        for j in range(i + 1, len(array3)):
            if array3[max_idx] > array3[j]:
                max_idx = j
        array3[i], array3[max_idx] = array3[max_idx], array3[i]
    print("Array 3 after selection sort:", array3)
array3 = [5, 99, 48, 15, 67]
select_sort(array3)



"""
"""
#Insertion Sort: descending
#4.[38, 82, 25, 74, 13] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into descending
#order.

array4 =  [38, 82, 25, 74, 13]
def insertsort_des(array4):
    print("Array 4 before Insertion Sort in Descending:")
    print(array4)
    for i in range(1, len(array4)):
        key = array4[i]
        j = i - 1
        while j >= 0 and key < array4[j]:
            array4[j + 1] = array4[j]
            j -= 1
        array4[j + 1] = key
    print("Array 4 after Insertion Sort in Descending:", array4)
array4 =  [38, 82, 25, 74, 13]
insertsort_des(array4)

"""

#5.Copy all of the values from the
#second index and third index of the previous datasets into one
#dataset. After copying, sort the data into ascending order and descending
#order each order of the dataset is inserted into a separate list/array.

arrays = [12, 78, 91, 34,62,599, 48, 82, 25]
print("In Ascending order:")
print(arrays)
for i in range(1, len(arrays)):
    key = arrays[i]
    j = i - 1
    while j >= 0 and key < arrays[j]:
        arrays[j + 1] = arrays[j]
        j -= 1
    arrays[j + 1] = key

arrays = [12, 78, 91, 34,62,599, 48, 82, 25]
for i in range(1, len(arrays)):
    key = arrays[i]
    j = i - 1
    while j >= 0 and key < arrays[j]:
        arrays[j + 1] = arrays[j]
        j -= 1
    arrays[j + 1] = key
    print("In Descending order:")
    print(arrays)


"""
#6.Create a new list/array or values copying all of
#the values from item number 1 to 4. Implement the Selection
#Sort Algorithm and sort the data into ascending order.
lists = [23,89, 7, 56, 44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13]
print("Lists before Selection Sort:")
print(lists)
for i in range(len(lists)):
    min_idx = i
    for j in range(i + 1, len(lists)):
        if lists[min_idx] < lists[j]:
            min_idx = j
    lists[i], lists[min_idx] = lists[min_idx], lists[i]
print("Selection sort in Descending order:")
print(lists)
"""

#7.Print the even and odd values of the
#list/array created in item number 6.
lists = [23,89, 7, 56, 44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13]


