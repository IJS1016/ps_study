# 65부터 90까지, chr()
# 우하좌상
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
n, m = map(int, input().split())
didx = 0

mmap = [[0 for _ in range(m)] for _ in range(n)]

cn = 0
flag = 0
ny, nx = 0, 0

def is_in_range(ty, tx) :
    return 0 <= ty < n and 0 <= tx < m

while flag < 3 :
    mmap[ny][nx] = chr(cn + 65)
    dy, dx = directions[didx]

    ty = ny + dy
    tx = nx + dx

    # 순서 주의
    if is_in_range(ty, tx) and mmap[ty][tx] == 0 : 
        ny, nx = ty, tx
        cn = (cn + 1) % 26
        flag = 0
    else :
        didx = (didx + 1) % 4
        flag += 1

for m in mmap :
    print(" ".join(map(str, m)))
