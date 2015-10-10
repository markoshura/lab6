input=open('input.txt', 'r')
output= open('output.txt', 'w')
N = int(input.readline())
s = list(map(int, input.readline().split()))
lmin = -1
for i in range(N):
    if s[i] > 0:
        continue
    itap = i
    tap = s[i]
    while itap + 1 < len(s):
        itap += 1
        if s[itap] == -tap:
            if lmin == -1 or lmin > len(s[i:itap]):
                lmin = len(s[i:itap])
if lmin == -1:
    print(0, file=output)
else:
    print(lmin, file=output)
