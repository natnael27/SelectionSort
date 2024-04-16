def selection_sort(arr):
 n = len(arr)
 for i in range(n - 1):
 
 # Find the minimum element in the unsorted part of the array
  min_index = i
  for j in range(i + 1, n):
     if arr[j] < arr[min_index]:
      min_index = j
 
 # Swap the found minimum element with the first element of the unsorted part
  arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [27, 34, 88, 1, 99, 77, 9, 8, 47, 66]
print("Original array:", arr)

# Perform selection sort
selection_sort(arr)
print("Sorted array:", arr)