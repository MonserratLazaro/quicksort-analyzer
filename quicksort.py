# Quick Sort implementation with partition and swap.

# Swap function
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# Partition
def partition(array, low, high):
    pivot = array[high] # Choose the pivot (last element)
    i = low - 1  # Index of the smallest element
    
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)
    
    # Place the pivot in its correct position
    swap(array, i + 1, high)
    return i + 1 # Return its position

# QuickSort 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)  # Pivot index after partition
        
        # Sort to the left of the pivot
        quickSort(array, low, pi - 1)
        # Sort to the right of the pivot
        quickSort(array, pi + 1, high)
        