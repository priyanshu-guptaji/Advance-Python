def count_elements(arr):
    l = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= l:
            cnt += 1

    return cnt

arr = list(map(int, input().split()))
print(count_elements(arr))