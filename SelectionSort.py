# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
#The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.


my_array2 = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array2)
for i in range(n-1):
    min_index2 = i
    for j in range(i+1, n):
        if my_array2[j] < my_array2[min_index2]:
            min_index2 = j
    min_value2 = my_array2.pop(min_index2)
    my_array2.insert(i, min_value2)

print("Sorted2 array4:", my_array2)