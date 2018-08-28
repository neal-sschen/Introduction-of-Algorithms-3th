#1  for ( i=1 to (n-1)):                  c1(n-1)
#2     for j = i+1 to n:                  c2(n-1 + n-2 +...+1)=c2(n-1)n/2    
#3       if A[j] <  A[i]:                 c3(n-1 + n-2 +...+1)=c3(n-1)n/2
#4         (A[j],A[i])=(A[i],A[j])        c4(n-1 + n-2 +...+1)=c4(n-1)n/2


# best-case：c4 = 0；
# worse-case：c4 != 0;
