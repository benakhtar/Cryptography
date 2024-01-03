def euclidean(a,b):
    """Returns the greatest common divisor of a and b using the euclidean algorithm."""
    if a % b == 0 or b == 1: #if b divides a or b being 1 is now the gcd remaining, we return b
        return b
    else:
        return euclidean(b, a % b) #keep running the gcd until we get one of the two results to return
