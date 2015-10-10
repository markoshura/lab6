N=int(input())
A=[]
for x in range(N):
    A.append(int(input()))
k=N
for x in range (N):
    for y in range(N):
        if (A[x])==-(A[y]) and A[x]<0 and x!=y:
            if abs(x-y)<k:
                k=abs(x-y)
if k!=N:
    print (k)
