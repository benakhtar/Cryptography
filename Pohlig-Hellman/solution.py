from utils import *
def CRT(moduli, values):
    """Returns an intenger n such that n modulo moduli[i] = values[i].

    Input: moduli - a list of k coprime positive integers
           values - a list of k integers
    """
    c = values[0]
    m = moduli[0]
    for i in range (1, len(moduli)):
        y_i = values[i]
        m_i = moduli[i]
        right_hand_side = y_i%m_i
        right_hand_side = right_hand_side - c
        m_inverse = modular_inverse(m,m_i)
        y_i = (right_hand_side * m_inverse)%m_i
        c= c + m * y_i
        m = m * m_i
    return (c%m)



def q_power_dlog(g,h,p,q,e):
    """Returns the discrete logarithm of g modulo p of h, where g has
    order q^e modulo p."""
    #YOUR CODE GOES HERE
    exponent = pow(q, e-1)
    a = pow(g,exponent,p)
    b_0 = pow(h,exponent,p)
    x_0 = babysteps_giantsteps(a,b_0,p,q)
    x_i = []
    x_i.append(x_0)
    g_i_exponent = 0
    x_total = x_0
    g_inverse = modular_inverse(g, p)


    for i in range(1, e):
        g_i_exponent += x_i[i-1]*(q**(i-1))
        b_i_base = (h * pow(g_inverse,g_i_exponent,p))%p
        b_i_exponent = pow(q, (e-i-1))
        b_i = pow(b_i_base, b_i_exponent, p)
        x = babysteps_giantsteps(a,b_i,p,q)
        x_i.append(x)
        x_total += x * (q**(i))
    return x_total

def pohlig_hellman(g,h,p,prime_divisors):
    """Returns the discrete logarithm of h with respect to the base g modulo p,
    where p - 1 = q_1^e_1 * ... * q_t^e^_t, and prime_divisors = [[q_1,e_1],...,[q_t,e_t]].
    """
    #YOUR CODE GOES HERE
    prime_array = []
    y_array = []
    N = 1
    for i in range(0,len(prime_divisors)):
        prime_array.append((prime_divisors[i][0]**prime_divisors[i][1]))
        N = N * prime_array[i]
    for i in range(0, len(prime_divisors)):
        bottom_exponent = prime_array[i]
        exponent = int(N//bottom_exponent)
        g_i = pow(g, exponent, p)
        h_i = pow(h, exponent, p)
        y_i = q_power_dlog(g_i,h_i,p,prime_divisors[i][0],prime_divisors[i][1])
        y_array.append(y_i)
    c = CRT(prime_array,y_array)
    return (c%N)
