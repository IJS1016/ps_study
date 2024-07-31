# 낼 복습하기
# / 코드에서 쓸 떄 '//'로 써줘야함
N = int(input())
mirrors = []
for _ in range(N) :
    mirrors.append(input().replace('\\','|'))
K = int(input())

# 방향 하좌상우
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def get_start(K) :
    # 시작 위치
    # n // 3으로 나눠서 d_idx 설정
    d_idx = (K - 1) // N

    # x 좌표 구하기, y 좌표는 여기서 +N-1 더하기
    start_points = [0] * N
    tmp = [x for x in range(1, N-1)]
    start_points += tmp
    start_points += [N - 1] * N
    start_points += reversed(tmp)

    K = K - (K // N) - 1
    y = start_points[K]
    x = start_points[(K + (N - 1)) % len(start_points)]
    # 복잡하게 생각하지 말고, 케이스가 적은 경우는 if 문으로 나눠서 구현하는게 더 빠름

    return y, x, d_idx

def check_inside_mmap(y, x) :
    if (0 <= y < N and 0 <= x < N) :
        return True
    return False
    #  return 0 <= x and x < n and 0 <= y and y < n 이런식으로 바로 return 때려줘도 됨

y, x, d_idx = get_start(K)
# '\\'->'|' -1, '/' +1
# 범위 벗어날 때까지 count
cnt = 0
while (check_inside_mmap(y, x)):
    d_idx = (d_idx + 2) % 4
    mirror = mirrors[y][x]
    if (d_idx in [0, 2] and mirror == '|') or (d_idx in [1, 3] and mirror == '/') :
        d_idx = (d_idx + 1) % 4
    else :
        d_idx = (d_idx + 3) % 4
    dy, dx = directions[d_idx]
    y += dy
    x += dx
    cnt += 1

print(cnt)