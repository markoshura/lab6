input=open('input.txt', 'r')
output=open('output.txt', 'w')
data = list(map(int, input.readline().split()))
N = data[0]
K = data[1]
rest = [0 for i in range(N)]
for i in range(K):
    vvod = list(map(int, input.readline().split()))
    doljnik = vvod[0]-1
    creditor = vvod[1]-1
    summa = vvod[2]
    rest[doljnik] -= summa
    rest[creditor] += summa
print(' '.join(map(str, rest)), file=output)
