input=open('input.txt', 'r')
output=open('output.txt', 'w')
data = list(map(int, input.readline().split()))
k = data[0]
n = data[1]
min = [-1 for i in range(n)]
for i in range(k):
    Z= list(map(int, input.readline().split()))
    for j in range(n):
                
        if Z[j] < min[j] or min[j] == -1:
            min[j] = Z[j]
print(' '.join(map(str, min)), file=output)
