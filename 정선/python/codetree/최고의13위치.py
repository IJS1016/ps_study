N = int(input())
mmap = []

for _ in range(N) :
    mmap.append(list(map(int, input().split())))

result = 0

for i in range(N-2) :
    for j in range(N) :
        tmp = mmap[j][i] + mmap[j][i+1] + mmap[j][i+2]
        if result < tmp :
            result = tmp

print(result)
