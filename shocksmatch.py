def sockMerchant(arr):
    socks = {}

    for sock in arr:
        socks[sock] = socks.get(sock, 0) + 1

    pairs = 0

    for sock in socks:
        pairs += socks[sock] // 2

    return pairs


arr = list(map(int, input().split()))
print(sockMerchant(arr))