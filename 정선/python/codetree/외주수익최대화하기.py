n = int(input())

jobs = []
for _ in range(n) :
    jobs.append(list(map(int, input().split())))

cases = []
def cal_max_money(d, money) :
    if d == n :
        return cases.append(money)
    t, p = jobs[d]
    if d + t <= n :
        cal_max_money(d + t, money + p)
    if d + 1 <= n :
        cal_max_money(d + 1, money)

cal_max_money(0, 0)
print(max(cases))

