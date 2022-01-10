def fact(n):
    """
    >>>fact(0)
    1
    >>>fact(1)
    1
    >>fact(3)
    6
    >>>fact(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def sums(n):
    if n == 0:
        return 0
    else:
        return n + sums(n-1)
    
def count_up(n):
    """Prints the numbers from 1 to n.
    >>> count_up(1)
    1
    >>> count_up(2)
    1
    2
    >>> count_up(4)
    1
    2
    3
    4
    """
    if n == 1:
        print(1)
    else:
        count_up(n-1)
        print(n)
        
        
        
def count_up2(n):
    if n>1:
        count_up2(n-1)
    print(n)
    
def sum_digits(n):

    if n < 10:
        return n
    elif n < 100:
        return (n%10) + n//10
    else:
        return n % 10 + sum_digits(n//10)
    
    
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
       