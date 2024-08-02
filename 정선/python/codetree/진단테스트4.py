# for 문 변수 중복으로 써서 out of range 발생
# 변수 중복으로 쓴거 없는지 항상 신경쓰기
n = int(input())

tmp = [1 for _ in range(n)]
print("".join(map(str, tmp)))

while tmp != [3 for _ in range(n)] :
    tmp[-1] += 1
    for i in range(n-1, 0, -1) :
        tmp[i-1] += tmp[i] // 4
        if tmp[i] % 4 == 0:
            tmp[i] = 1

    cnt = 0
    flag = True
    for j in tmp :
        if j == 3 :
            cnt += 1
        if cnt > 2 :
            flag = False
            break

    if flag :
        print("".join(map(str, tmp)))
