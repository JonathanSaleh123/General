from operator import add,pow

def mynumber(x,y):
    """makes x the power of y and adds 5
>>> mynumber(10,3)
1005
>>> mynumber(5,4)
630
>>> mynumber(1,10)
6
"""
    return add(5,pow(x,y))

