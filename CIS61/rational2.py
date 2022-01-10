from math import gcd
# Version 1
# Representation
def rational(n, d):
    """A representation of the rational number N/D."""
    gcd_a_b = gcd(n,d)
    return {"numer":n//gcd_a_b, "denom":d//gcd_a_b}

def numer(x):
    """Return the numerator of rational number X."""
    return x["numer"]

def denom(x):
    """Return the denominator of rational number X."""
    return x["denom"]

def mul_rational(x,y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * ny, dx * dy)
    
    
def print_rational(x):
    print(numer(x),"/",denom(x))
    
def rationals_are_equal(x, y):
    """True if rational numbers X and Y are equal."""
    return numer(x)*denom(y) == numer(y)*denom(x)