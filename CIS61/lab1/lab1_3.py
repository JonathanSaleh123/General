def buy_food(hungry,money):
    """Should buy food
    >>> buy_food (True,10)
    False
    >>> buy_food (False,100)
    False
    >>> buy_food (True,20)
    True
    """
    return hungry and money>10
