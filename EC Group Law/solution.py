def add(P,Q,A,B,p):
    """Returns P+Q on the curve y^2=x^3+Ax+b over Fp."""
    # YOUR CODE GOES HERE
    if Q == None:
        return P
    if P == None:
        return Q
    xP, yP = P
    xQ, yQ = Q
    if xP == xQ and yP == (-yQ)%p:
        return None
    if xQ != xP:
        m_top = (yP-yQ)%p
        m_bottom = (xP-xQ)%p
        gcd, x, y = extended_euclidean(m_bottom, p)
        m_bottom_inverse = x%p
        m = (m_top * m_bottom_inverse)%p
    else:
        m_top = (3 * xP ** 2 + A) % p
        m_bottom = (2 * yP)%p
        gcd, x, y = extended_euclidean(m_bottom, p)
        m_bottom_inverse = x % p
        m = (m_top * m_bottom_inverse) % p
    xR = (m * m - xP - xQ)%p
    negative_yR = (m * (xP - xR) - yP)%p
    return (xR,negative_yR)


def dbl(P,A,B,p):
    """Returns 2P on the curve y^2=x^3+Ax+b over Fp."""
    # YOUR CODE GOES HERE
    xP, yP = P
    m_top = (3 * xP ** 2 + A) % p
    m_bottom = (2 * yP) % p
    gcd, x, y = extended_euclidean(m_bottom, p)
    m_bottom_inverse = x % p
    m = (m_top * m_bottom_inverse) % p
    xR = (m * m - xP - xP) % p
    negative_yR = (m * (xP - xR) - yP) % p
    two_P = (xR, negative_yR)

    return two_P





def neg(P,p):
    """Returns -P on the curve y^2=x^3+Ax+b over Fp."""
    # YOUR CODE GOES HERE
    xP, yP = P
    return (xP%p,-yP%p)


def smul(n,P,A,B,p):
    """Returns nP on the curve y^2=x^3+Ax+b over Fp."""
    # YOUR CODE GOES HERE
    Q = P
    R = None
    if n < 0:
        P = neg(P,p)
        Q = P
        n = abs(n)
    while n > 0:
        if n == 0:
            break
        if n % 2 == 1:
            R = add(R,Q,A,B,p)
        Q = dbl(Q, A, B, p)
        n = n // 2
    return R

def extended_euclidean(a,b):
    """Returns gcd(a,b) along with integers s,t such that gcd(a,b)=as+bt using
     the extended euclidean algorithm."""
    # YOUR CODE GOES HERE
    r_previous = a
    r = b
    s_previous = 1
    s = 0
    t_previous = 0
    t = 1
    while r != 0:
        q = r_previous // r
        r_next = r_previous % r
        r_previous = r
        r = r_next
        temp_s_previous = s_previous
        temp_s = s
        temp_t_previous = t_previous
        temp_t = t
        s_previous = s
        s = temp_s_previous - q*temp_s
        t_previous = t
        t = temp_t_previous - q*temp_t
    return r_previous, s_previous, t_previous

