input = open('input.txt', 'r')
output = open('output.txt', 'w')
s=input.readline()
d=input.readline()
k='0'
i=0
while i<len(d):
    j=0
    while j<len(d):
        if d[i]==d[j]  and i!=j:
            k=d[i]
        j+=2
    i+=2
output.write(k)


input.close()
output.close()
