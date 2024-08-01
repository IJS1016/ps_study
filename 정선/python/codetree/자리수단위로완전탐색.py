import sys

n = int(input())
A = list(map(int, input().split()))

result = sys.maxsize

for i in range(n) :
    tmp = 0
    for j in range(n) :
        if i != j :
            tmp += A[j] * abs(i-j)
    if tmp < result :
        result = tmp

print(result)