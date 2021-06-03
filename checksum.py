import numpy as np

checksums = np.zeros([1024, 3], np.uint8)
codewords = np.zeros([1024, ], np.uint64)

for x in range(1024):
    byte1 = x % 256
    byte2 = x // 256
    checksums[x, 0] = byte1 ^ byte2

    dec1 = x % 100
    dec2 = x // 100
    checksums[x, 1] = dec1 ^ dec2

    checksums[x, 2] = x//1000 + (x//100)%10 + (x//10)%10 + x%10

for i in range(3):
    unique, counts = np.unique(checksums[:, i], return_counts=True)
    distinct = dict(zip(unique, counts))
    print(distinct)

    print(np.mean(counts, axis=0))
    print(np.var(counts, axis=0))
