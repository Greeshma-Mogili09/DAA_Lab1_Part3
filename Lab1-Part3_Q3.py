def sort_array_with_swapped_elements(arr):
    n = len(arr)
    first_swap = None
    second_swap = None

    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if first_swap is None:
                first_swap = i
            else:
                second_swap = i + 1
                break

    
    arr[first_swap], arr[second_swap] = arr[second_swap], arr[first_swap]

    return arr

arr = list(map(int, input("Enter the array elements separated by space: ").split()))


sorted_arr = sort_array_with_swapped_elements(arr)
print("Sorted Array:", sorted_arr)
