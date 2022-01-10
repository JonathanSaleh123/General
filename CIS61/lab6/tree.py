
from typing import List


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

#Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True

def is_leaf(tree):
    return not branches(tree)

def count_nodes(t):
    """
    >>> t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> count_nodes(t1)
    5
    """
    if is_leaf(t):
        return 1
    
    total = 0
    for b in branches(t):
        total = total + count_nodes(b)
    return 1 + total

def count_nodes2(t):
    if is_leaf(t):
        return 1
    
    lst = [count_nodes2(b) for b in branches(t)]
    return len(lst) + 1 
# return sum(lst,1)

    
def count_leaves(t):
    """
    >>> t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> count_leaves(t1)
    3
    """
    
    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total = total + count_leaves(b)
    return total

def count_leaves(t):
    """
    >>> t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    >>> count_leaves(t1)
    3
    """
    
    if is_leaf(t):
        return 1
    total = 0
    lst = [count_leaves(b) for b in branches(t)]
    return sum(lst,0)


def collect_leaves(t):
    """
    >>> collect_leaves(t2):
    ['B','D','E']
    """
    if is_leaf(t):
        return [label(t)]
    
    lst = []
        
    for b in branches(t):
        lst = lst + collect_leaves(b)
        
    return lst

def collect_leaves2(t):
    """
    >>> collect_leaves(t2):
    ['B','D','E']
    """
    if is_leaf(t):
        return [label(t)]
    
    lst = [collect_leaves2(b) for b in branches(t)]
    
    return sum(lst,[])

def print_tree(t, indent=0):
    if is_leaf(t):
        print(" "*indent + str(label(t)))
    else:
        print(" "*indent+ str(label(t)))
        for b in branches(t):
            print_tree(b,indent+2)

def square_tree(t):
    if is_leaf(t):
        return tree(label(t)**2)
    lst = []
    
    for b in branches (t):
        lst = lst + [square_tree(b)]
        
    return tree(tree(label(t)**2), lst)

    
def square_tree2(t):
    return tree(label(t)**2, [square_tree2(b) for b in branches(t)])

def fib_tree(n):
    if n < 2:
        return tree(n)
    left = fib_tree(n-2) 
    right = fib_tree(n-1)
    
    lb = label(left) + label(right)
    
    return tree(lb,[left,right])

def tree_max(t):
    """Return the maximum label in a tree. 
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)]) 
    >>> tree_max(t) 
    10 
    """
    if is_leaf(t):
        return label(t)
    
    lst = []
    
    for b in branches(t):
        lst = lst + [tree_max(b)]
    
    return max(lst)

def find_path(tree, x): 
    """ >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)]) 
    >>> find_path(t, 5) 
    [2, 7, 6, 5] 
    >>> find_path(t, 10) # returns None 
    """ 
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        sub_path = find_path(b, x)
        if sub_path:
            return [label(tree)] + sub_path

    


def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and False otherwise.
    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul=tree('roots',[tree('branch1',[tree('leaf'),tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    "*** YOUR CODE HERE ***"
    
    return label(t) == 'acorn' or any(acorn_finder(b) for b in branches(t))
    
    
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears 
    in vals removed.  Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if label(t) in vals:
            return None
    return tree(label(t), [prune_leaves(b,vals) for b in branches(t) if prune_leaves(b,vals)!= None])

    

    
    

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t), [tree(i) for i in vals])
    else:
        lst = [sprout_leaves(b,vals) for b in branches(t)]
        return tree(label(t),lst)
    
    
    
    
def height(t): 
    """Return the height of a tree. 
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)]) 
    >>> height(t) 
    2 
    """
    if is_leaf(t):
        return 0
    for b in branches(t):
        height(b)
        
    return max([1 + height(b) for b in branches(t)])
    
    
    

def double_tree(t): 
    """Return a tree with the square of every element in t 
    >>> numbers = tree(1,
                       [tree(2,
                             [tree(3),
                              tree(4)]),
                       tree(5,
                            [tree(6,
                                  [tree(7)]),
                             tree(8)])]) 
    >>> print_tree(double_tree(numbers)) 
    2
      4
        6 
        8 
      10 
        12 
          14 
        16 
    """
    return tree(label(t)*2, [double_tree(b) for b in branches(t)])
    
    
    

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    
    if is_leaf(t1) and is_leaf(t2):
        return tree(label(t1)+label(t2))
    lst = []
    
    for b in branches (t1):
        for i in branches(t2):
            lst = lst + add_trees(b,i)
        
    return tree(label(lst),lst)

    return tree(label(t1)+label(t2), [add_trees(t1,t2) for b in branches(t2)])



