#Lab 4 - Template
# Question 1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.
    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    """
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return n + skip_add(n-2)
    
    
    


# Question 2
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    
    if n == 1: 
        return 1
    else:
        if n %2 == 0:
            print(int(n))
            return hailstone(n/2)
            
        elif n %2 != 0:
            print(int(n))
            return hailstone(n*3 + 1)
    
            
        
    
    

        
# Question 3
def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!
    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    """
    if n == 0:
        return 0
    elif n == 1:
        return term(n)
    else:
        return term(n) + summation(n-1,term)
    
    
    
# Question 4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n <= 1:
        return False
    else:
        def help(i):
            if n <= i :
                return True
            elif n % i == 0:
                return False
            else :
                return help(i+1)
        return help(2)
    
    
    
    
    
    
    
    
        


# Question 5
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
    
        
        
        
    
# Question 6
def count_stair_ways(n):
        
    def repeat(n):
        if n <=3 and n>0 :
            return n
        else:
            return repeat(n-1)+repeat(n-2)    
    return repeat(n)
  


# Question 7 (Optional)
def count_k(n, k):
    """ >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4) 
    8 
    >>> count_k(10, 3) 
    274
    >>> count_k(300, 1) # Only one step at a time 
    1 
    """
    if n ==0:
        return 1
    elif n<0:
        return 0
    else:
        i = 1
        total = 0
        while i <= k:
            total = total + count_k(n-i,k)
            i = i + 1
        return total  
            
        



# Question 8 (Optional)
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_upto(n//10, 10- n%10)
    
def count_upto(i,number):
    if i == 0:
        return 0
    elif i % 10 == number:
        return count_upto(i //10, number) + 1
    else:
        return count_upto(i//10, number)
    
    
def multiply(m,n):
    
    if n == 1: 
        return m
    else:
        return m + multiply(m, n-1)