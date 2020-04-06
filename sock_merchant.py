def sockMerchant(n, ar):
    if n == 0 or n == 1:
        return 0

    sock_dict = {}
    for i in range(0, n):
        if ar[i] in sock_dict.keys():
            sock_dict[ar[i]] += 1
        else:
            sock_dict[ar[i]] = 1
    pairs = 0
    for color, num in sock_dict.items():
        pairs += num // 2
    return pairs 

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))