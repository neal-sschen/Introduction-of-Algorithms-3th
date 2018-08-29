def P(A):
    for i in range(1:(len(A)-1)):
        Q(A,0,i-1,A[i])

def Q(A,m,k,v):
    if m < k:
        r = int((m+k)/2)
        if A[r] < v:
            Q(A,r+1,k,v)

        elif A[r] > v:
            A[r+2:k+2]=A[r+1:k+1]
            Q(A,m,r,v)
    elif m == k:
        if A[m] <= v:
            A[m+1] = v
        else:
            [A[m],A[m+1]]=[v,A[m]]

A = [20,56,48,121,232,12,1,0,1,45,56,81]
P(A,0,len(A)-1)
print(A)
