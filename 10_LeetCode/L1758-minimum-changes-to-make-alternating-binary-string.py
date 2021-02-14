def minOperations(s):
    i1 = ['0' if i % 2 else '1' for i in range(len(s))]
    i2 = ['1' if i % 2 else '0' for i in range(len(s))]
    c1, c2 = 0, 0
    for v1, v2 in zip(i1, s):
        if v1 != v2: c1 += 1
    for v1, v2 in zip(i2, s):
        if v1 != v2: c2 += 1
    return min(c1, c2)


s = "0100"
s = "10"
s = "1111"

print(minOperations(s))