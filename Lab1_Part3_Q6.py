def has_sum_quadratic(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == K:
                return True
    return False
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
K = int(input("Enter the target sum K: "))

result = has_sum_quadratic(arr, K)
print("Does the array contain two numbers that sum up to", K, "?", result)



def has_sum_nlogn(arr, K):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == K:
            return True
        elif arr[left] + arr[right] < K:
            left += 1
        else:
            right -= 1
    return False

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
K = int(input("Enter the target sum K: "))

result = has_sum_nlogn(arr, K)
print("Does the array contain two numbers that sum up to", K, "?", result)
