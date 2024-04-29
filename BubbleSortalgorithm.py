#Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
my_array = [64, 34, 25, 12,22, 11, 90, 5]
n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)



#Imagine that the array is almost sorted already, with the lowest numbers at the start, like this for example


my_array2 = [7, 3, 9, 12, 11]
n = len(my_array2)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array2[j] > my_array2[j+1]:
            my_array2[j], my_array2[j+1] = my_array2[j+1], my_array2[j]
            swapped = True
        if not swapped:
            break

print("Sorted array2:", my_array2)