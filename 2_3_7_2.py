def Merge(A,p,q,r):
    L = A[p:(q+1)]
    R = A[(q+1):r+1]

    L.append(10000)
    R.append(10000)

    k = p
    i = 0
    j = 0

    while(k <= r):
        if L[i] < R[j]:
            A[k] = L[i]
            k = k+1
            i = i+1
        else:
            A[k] = R[j]
            k = k+1
            j = j +1

def Merge_Sort(A,p,r):
    if p < r:
        q = int((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merge(A,p,q,r)


A = [3,41,52,26,38,57,9,49,52]



Merge_Sort(A,0,len(A)-1)

print(A)


def P(A,x):
    i = 0
    r = len(A)-1
    while i < r:
        k = x - A[i]
        j = i+1
        if find_x(A,j,r,k)==1:
            print('Yes')
            return 'Yes'
        i = i+1
    print('No')
    return 'No'

def find_x(A,k,m,r):

    if k <= m:
        y = int((k+m)/2)
        if A[y] == r:
            print(r)
            return 1
        elif A[y] < r:
            return(find_x(A,y+1,m,r))
        else:
            return(find_x(A,k,y-1,r))
    else:
          return 0

x = 102

P(A,x)
