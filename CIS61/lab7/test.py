from typing import Counter


stuff = 10
def f():
    x = stuff
    x = x+1
    print(x)
    

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount>balance:
            return"Insufficient Funds"
        else:
            balance = balance - amount
        return balance
    return withdraw


def add_this_many(x, el, lst): 
    """ Adds el to the end of lst the number of times x occurs in lst. 
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst) 
    >>> lst 
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst) 
    >>> lst 
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
   
    lst_size = len(lst)
    for i in range(lst_size):
        if lst[i] == x:
            lst.append(el) 
        
    
    
def group_by(s, fn): 
    """ 
    >>> group_by([12, 23, 14, 45], lambda p: p // 10) 
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    lst = [i for i in s]
    lst.sort(key=fn)
    dic ={}
    for i in lst:
        if fn(i) in dic:
            dic[fn(i)].append(i)
        else:
            dic[fn(i)] = [i]
    return dic
    
    
    
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    count = 0
    def add(x):
        nonlocal sum
        nonlocal count
        sum = x + n + count
        count +=1 
        return sum
    return add

def memory(n): 
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def func(fn):
        nonlocal n
        n = fn(n)
        return n
    return func
        
    
def make_fib():
    """
    Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    end = 0
    current = 0
    last = 0
    def func():
        
        nonlocal end
        nonlocal current
        nonlocal last
        end = current
        current,last  = current + last, current
        if current == 0:
            current += 1
        return end
    return func
    
    
def make_withdraw(balance, password):
    """
    Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    lst = []
    passcount = 0
    def withdraw(amount,key):
        nonlocal balance, password, lst, passcount
        if passcount  == 3:
            message = "Your account is locked. Attempts: " + str(lst)
            return message
        else:
            if key == password:
                if amount>balance:
                    return"Insufficient funds"
                else:
                    balance = balance - amount
                return balance
            else:
                lst.append(key)
                passcount +=1
                return "Incorrect password"        
    return withdraw
    
    
    
    

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10
    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"

    message = withdraw(0, old_password)
    if type(message)== str:
        return message
    
    def withdraw_v2(amt, pwd):
        if pwd == new_password:
            return withdraw(amt, old_password)
        else:
            return withdraw(amt, pwd)
        
    return withdraw_v2
    




