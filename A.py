input=open('input.txt', 'r')
output=open('output.txt', 'w')
N = int(input.readline())
s = list(map(int, input.readline().split()))
i=0
k=0
while i<N:
    j=0
    while j<N:
        if i!=j and (s[i]==s[j]):
            k=s[i]
        j+=1
    i+=1

print(k, file=output)
