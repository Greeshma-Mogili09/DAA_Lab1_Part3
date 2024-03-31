def max_product_pair(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"

   
    first_max = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])

    
    first_min = min(arr[0], arr[1])
    second_min = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
        elif arr[i] > second_max:
            second_max = arr[i]

        if arr[i] < first_min:
            second_min = first_min
            first_min = arr[i]
        elif arr[i] < second_min:
            second_min = arr[i]

    if first_max * second_max > first_min * second_min:
        return first_max, second_max
    else:
        return first_min, second_min

arr = list(map(int, input("Enter the array elements separated by space: ").split()))

pair = max_product_pair(arr)
print("Pair with maximum product:", pair)
print("Maximum product:", pair[0] * pair[1])
