N = int(input())
cows = list(map(int, input().split()))

result = 0
for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if cows[i] <= cows[j] <= cows[k] :
                result += 1
print(result)