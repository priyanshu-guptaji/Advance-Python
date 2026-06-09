def count_frequency(arr, k):
    count = 0

    for i in arr:
        if i == k:
            count += 1

    return count

print("Enter Elements in array")
arr = list(map(int, input().split()))

k = int(input("Enter the element to find frequency: "))
result = count_frequency(arr, k)

print("Frequency:", result)