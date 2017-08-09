def trailingZeros(n):
    count = 1
    res = 0
    while True:
        temp = n // (5 ** count)
        if temp == 0:
            break
        res += temp
        count += 1
    return res

print(trailingZeros(111))
