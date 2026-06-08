arr = [1, 2, 7, 16, 12]
k = 2

n = len(arr)
k = k % n

arr = arr[n-k:] + arr[:n-k]

print(arr)