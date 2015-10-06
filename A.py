input=open('input.txt', 'r')
output=open('output.txt', 'w')
N = int(input.readline())
s = list(map(int, input.readline().split()))

f = False

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if s[i] == s[j]:
            f = True
            break
    if f:
        break
print(s[i], file=output)
