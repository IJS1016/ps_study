import math

n = int(input())
customers = list(map(int, input().split()))
tl, tm = map(int, input().split()) 

result = 0
for c in customers :
    tm_n = 0

    c = c - tl
    if c >= 0 :
        tm_n = c / tm
        tm_n = math.ceil(tm_n)
    
    result = result + 1 + tm_n

print(result)