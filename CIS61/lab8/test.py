def fib(n):
    prev, curr = 0, 1
    k = 0
    while k < n:
        prev, curr = curr, prev + curr
        k += 1
    return prev

def fib_iter(n):
    """
    >>> x = fib_iter(4)
    >>> next(x)
    0
    >>> next(x)
    1
    >>> next(x)
    1
    >>> next(x)
    2
    """
    prev, curr = 0, 1
    lst = [prev,curr]
    
    k = 2
    while k<n:
        prev, curr = curr, prev + curr
        lst +=[curr]
        k +=1
        
    return iter(lst)

def division(x, y):
    try:
        result = x/y
    except 0:
        print("Can't divide by 0")
        return 0
    return result

def negate(x):
    while True:
        x = -x
        yield x
        
def gen_list(lst):
    yield lst
    
def naturals():
    x = 0
    while True:
        yield x
        x +=1
def gen_list2(lst):
    yield from lst
    
def countdown(k):
    if k == 0:
        yield 'Blast off'
    else:
        yield k
        yield from countdown(k-1)
        
    