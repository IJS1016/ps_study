N, T = map(int, input().split())
orders = input()
mmap = []

for _ in range(N) :
    mmap.append(list(map(int, input().split())))

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ny, nx = N // 2, N // 2
idx = 0
result = mmap[ny][nx]

def in_range(y, x) :
    return 0 <= y < N and 0 <= x < N

for o in orders :
    if o == 'F' :
        dy, dx = directions[idx]
        if in_range(ny + dy, nx + dx) :
            ny += dy
            nx += dx
            result += mmap[ny][nx]

    elif o == 'R' :
        idx = (idx + 1) % 4
    else :
        idx = (idx + 3) % 4

print(result)