string = input()
l = len(string)

result = 0

for i in range(l) :
    if string[i] == '(' :
        for j in range(i+1, l) :
            if string[j] == ')' :
                result += 1

print(result)
