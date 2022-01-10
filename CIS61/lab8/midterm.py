def print_moar(stuff):
    i = 0
    while stuff and i < 2:
        stuff = print(stuff, print('colin'))
        i += 1
    return stuff

def square(x):
    return x * x

def argentina(n):
    print(n)
    if n > 0:
        return lambda k: k(n+1)
    else:
        return 1 / n
def make_digit_remover(i):
    """
    
    >>> remove_two = make_digit_remover(2)
    >>> remove_two(232018)
    23
    >>> remove_two(23)
    0
    >>> remove_two(99)
    99
    """
    def remove(n):
        lst = []
        for elem in n:
            lst += n
        
        return lst[:i]
    
    
def map_mut(f, L):
    """Mutatively maps f onto each element in L.

    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    "*** YOUR CODE HERE ***"
