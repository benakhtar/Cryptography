from math import sqrt, floor
def dlog(g,h,p,N=None):
    """Returns the discrete logarithm of h with respect to
    the base b modulo p, where g has order N."""
    if not N: N = p-1
    #YOUR CODE GOES HERE
    y = 1
    x = 0
    h = h%p
    while y!= h:
        y = (y * g) % p
        x += 1
    return x
    #
def indices_of_match(L1, L2):
    """Returns the indices of a common element of the lists L1
    and L2, i.e. a tuple (i,j) such that L1[i] == L2[j]."""
    #YOUR CODE GOES HERE
    N = len(L1)
    L3 = L1.copy()
    L3.sort()
    L4 = L2.copy()
    L4.sort()
    p3, p4 = 0, 0
    p1,p2 =-1,-1
    while (p3 < N-1 and p4 < N-1):
        if L3[p3] == L4[p4]:
            break
        if L3[p3] < L4[p4]:
            p3+= 1
        if L3[p3] > L4[p4]:
            p4+=1
    for x in range(0, N):
        if L1[x] == L3[p3]:
            p1 = x
        if L2[x] == L4[p4]:
            p2 = x
    if p1!= -1 and p2!= -1:
        return (p1, p2)
    return False, False
    #
def babysteps_giantsteps(g,h,p,N=None):
    """Returns the discrete logarithm of h with respect to
    the base b modulo p, where g has order N, using Shanks'
    babysteps-giantsteps algorithm."""
    if not N: N = p-1
    #YOUR CODE GOES HERE
    n = 1 + floor(sqrt(N))
    babysteps = []
    giantsteps = []
    babysteps.append(1)
    giantsteps.append(h)
    for i in range (1, n):
        babysteps.append((g * babysteps[i-1])%p)
        giantsteps.append(((pow(g,-n,p)) * giantsteps[i - 1]) % p)
    i,j = indices_of_match(babysteps, giantsteps)
    if i!=False and j!=False:
        return (i + j * n)
    return False
    #