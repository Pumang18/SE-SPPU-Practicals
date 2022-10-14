"""Write a python program to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order
using quick sort and display top five scores."""

n = int(input("Enter Total Count: "))
percentage = []
for i in range(0, n):
    r = float(input("Enter Percentage of Student: "))
    percentage.append(r)
print(percentage)

# Sorting By Quick Sort


def partition(array, low, high):

    p = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= p:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)




size = len(percentage)

quickSort(percentage, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(percentage)

last_five= (percentage[-1:-6:-1])
print("Top Five Marks Are: ")
print(last_five)