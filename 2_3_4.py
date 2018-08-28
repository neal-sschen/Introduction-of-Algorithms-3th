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

A = [34,67,12,45,67,89,12,15,42]
P(A)
print(A)
