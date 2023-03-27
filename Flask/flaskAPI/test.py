def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [3, 6, 1, 9, 2, 8, 4, 7, 5]
sorted_list = quick_sort(my_list)
print(sorted_list)