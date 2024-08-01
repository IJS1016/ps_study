R, C = map(int, input().split())

mmap = []

for _ in range(R) :
    mmap.append(input().split(' '))

result = 0

def go(ny, nx, cnt) :
    global result
    if cnt > 3 :
        return
    if ny == R-1 and nx == C-1 and cnt == 3 :
        result += 1 
        return

    nc = mmap[ny][nx]
    for ty in range(ny+1, R) :
        for tx in range(nx+1, C) :
            if mmap[ty][tx] != nc :
                go(ty, tx, cnt+1)

go(0, 0, 0)
print(result)