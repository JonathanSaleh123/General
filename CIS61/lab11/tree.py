class Tree:
    def __init__(self,label,branches = []):
        for b in branches:
            assert isinstance(b,Tree)
        self.label = label
        self.branches = branches
        
    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches == []:
            return 'Tree(' + str(self.label) + ')'
        else:
            return 'Tree(' + str(self.label) + ', ['+ ''.join(str(b) for b in self.branches) + '])'
    

def print_tree(t, indent=0):
    print(" "*indent + str(t.label))
    for b in t.branches:
        print_tree(b, indent+1)
        
def map_tree(t, f):
    t.label = f(t.label)
    for b in t.branches:
        map_tree(b,f)
        

class A:
    def __str__(self):
        return "A object"
    
    def __repr__(self):
        return "A object"
    
    
    
class Link():
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link(' + repr(self.first)+')'
        else:
            return 'Link(' + repr(self.first)+ ',' + repr(self.rest)+ ')'
    
    def __str__(self):
        s = '<'
        while self.rest is not Link.empty:
            s += str(self.first) + ',' 
            self = self.rest
        return s + str(self.first) + '>'
    
    def __eq__(self,other):
        if self.first != other.first:
            return False
        return self.rest == other.rest
    
    def __contains__(self,x):
        if self.first == x:
            return True
        return x in self.rest
        
                
def sum_link(lnk):
    """Return sum of elements in lnk
    """
    if lnk is Link.empty:
        return 0
    
    return lnk.first + sum_link(lnk.rest)


def display_link(lnk):
    string = "< "
    
    while lnk is not Link.empty:
        if isinstance(lnk.first,Link):
            elem = display_link(lnk.first)
        else:
            elem = str(lnk.first)
        string += elem+" "
        lnk = lnk.rest
        
    return string + ">"


def map(f, lnk):
    if lnk is Link.empty:
        return Link.empty
    return Link(f(lnk.first),map(f,lnk.rest))

def map_link_mute(f, lnk):
    if lnk is Link.empty:
        return
    
    lnk.first = f(lnk.first)
    map_link_mute(f, lnk.rest)
    
def map_link_mute(f, lnk):
    while lnk is not Link.empty:
        lnk.first = f(lnk.first)
        lnk = lnk.rest
