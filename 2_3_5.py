def P(A):
    if len(A) > 1:
        B = A[0:-1]
        c = A[-1]

        P(B)

        i = 0

        while i <= (len(B)-1):
            if B[i] > c:
                A[i] = c
                A[i+1:] = B[i:]
                break
            else:
                A[i] = B[i]
                i = i+1

def Search(A,p,q,r):
    if p <= q:
        k = int((p+q)/2)
        print(k)
  
        if A[k] < r:
            return(Search(A,k+1,q,r))
            print('q')
        elif A[k] > r:
            return(Search(A,p,k-1,r))
            print('p')
        else:
            print('k')
            return k








A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,12,43,6546,12,1212,4343,23123,]
#A = [34,67,12,45,67,89,12,15,42]
P(A)
print(A)

k = Search(A,0,len(A)-1,15)
print(k)

