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
    print(r_previous,s_previous,t_previous)
    return r_previous, s_previous, t_previous

    #
def square_and_multiply(g,x,m):
    """Returns g^x modulo m using the square-and-multiply algorithm."""
    b = 1
    a = g
    while x != 0:
        if x == 0:
            break
        if x % 2 == 1:
            b = (b * a) % m
        a = (a*a) % m
        x = x // 2
    return b
def modular_inverse(a,m):
    """Returns an integer b such that a*b=1 mod m if gcd"""
    # YOUR CODE GOES HERE
    r_previous = a
    r = m
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
    return s_previous
    #


