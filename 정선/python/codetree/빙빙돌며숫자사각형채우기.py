n, m = map(int, input().split())
mmap = [[0 for _ in range(m)] for _ in range(n)]

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
d_idx = 0
ny, nx = 0, 0
cnt = 1
mmap[0][0] = cnt
def is_inrange(y, x) :
    return 0 <= y < n and 0 <= x < m

while (cnt < (n * m)) :
    dy, dx = directions[d_idx]
    ty = ny + dy
    tx = nx + dx
    if is_inrange(ty, tx) and mmap[ty][tx] == 0 :
        ny = ty
        nx = tx
        cnt += 1
        mmap[ny][nx] = cnt

    else :
        d_idx = (d_idx + 1) % 4

for m in mmap :
    print(" ".join(map(str, m)))