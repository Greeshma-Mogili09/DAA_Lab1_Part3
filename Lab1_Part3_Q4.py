def segregate_0_and_1(arr):
    count = [0, 0]  

    for num in arr:
        count[num] += 1

    i = 0
    for i in range(2):
        for _ in range(count[i]):
            arr[i] = i
            i += 1

    return arr


arr = list(map(int, input("Enter the binary array elements separated by space (0's and 1's): ").split()))

segregated_array = segregate_0_and_1(arr)
print("Segregated array:", segregated_array)
