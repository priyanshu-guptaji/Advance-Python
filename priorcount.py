def count_elements(arr):
    l = arr[0]
    cnt = 0

    for i in arr:
        if i >= l:
            cnt += 1

    return cnt

arr = list(map(int, input().split()))
print(count_elements(arr))