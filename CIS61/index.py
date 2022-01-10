def abs_val(x):
    if x > 0 : 
        return x
    elif x < 0:
        return -x
    else:
        return 0
    
def f(x):
    if x < 0:
        return "negative"
    elif x %2 == 0 :
        return " Even number"
    elif x % 3 == 0 :
        return "Can be divided by 3"
    
#f(6) returns Even number, as it doesnt go trough other statements.

def abs_val2(x):
    if x >= 0:
        return x
    
        return -x
#can Also work

def fib(n):
    
    prev, curr = 0, 1
    
    k = 2
    
    while k <= n:
        nxt = prev + curr
        prev = curr
        curr = nxt
        k = k + 1

    return curr




    
    