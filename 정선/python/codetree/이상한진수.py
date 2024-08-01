a = input()

result = 0
for i in range(len(a)) :
    if a[i] == '0' :
        tmp = a[:i] + '1' + a[i+1:]
    else :
        tmp = a[:i] + '0' + a[i+1:]
    tmp_n = int(tmp, 2) 

    if result < tmp_n :
        result = tmp_n

print(result)