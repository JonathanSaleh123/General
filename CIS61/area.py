from math import pi, sqrt

def area(r, const):
    assert r>0, "r should be positive"
    return const * r * r

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3)/2)




def identity(x):
    return x

def cube(x):
    return pow(x,3)

def square(x):
    return x * x




#term means a function, that will call some expression to k

def summation(n,term):
    total, k = 0, 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total


def sum_naturals(n):
    
    return summation(n,identity)

def sum_naturals(n):
    
    return summation(n,lambda x: pow(x,1))


def sum_squares(n):
    
    return summation(n, lambda x: pow(x,2))

def sum_cubes(n):
    

    return summation(n, lambda x: pow(x,3))

def add_to(n):
    def adder(k):
        return n + k
    return adder


