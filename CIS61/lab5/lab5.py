def add_chars(w1,w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.
    You may assume that w1 is a subsequence of w2.
    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """
    "*** YOUR CODE HERE ***"
    if not w1:
        return w2
    elif w1[0] == w2[0]:
        return add_chars(w1[1:], w2[1:])
    else:
        return w2[0] + add_chars(w1, w2[1:])
        
    
   
    
def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    "*** YOUR CODE HERE ***"
    return min(d, key=d.get) 


def flatten(lst):
    """Returns a flattened version of lst.
    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    new_lst = []
    for item in lst:
        if type(item) != list:
            new_lst += [item] 
        else:
            new_lst += flatten(item)      
    return new_lst      
    """    
    if not lst :
            return []
        elif len(lst) != 0 and type(lst[0]) == list:
            return flatten(lst[0]) + flatten(lst[1:])
        elif len(lst) != 0 and type(lst[0]) != list:
            return [lst[0]] + flatten(lst[1:])
        else:
            return []
    
                    if not lst:
                    return []
            elif type(lst[0]) == list:
                return flatten(lst[0]) + flatten(lst[1:])
            else:
                return [lst[0]] + flatten(lst[1:])
    """   
                
        
            
        
    
 
 
