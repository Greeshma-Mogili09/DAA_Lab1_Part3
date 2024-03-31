def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)

    return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


arr = list(map(int, input("Enter the array elements separated by space: ").split()))

sorted_arr, inversions = merge_sort(arr)
print("Sorted Array:", sorted_arr)
print("Number of inversions:", inversions)
