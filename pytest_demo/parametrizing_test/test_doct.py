import doctest

def multiply(a,b):
    """
    function:两个数相乘
    >>> multiply(4,3)
    12
    >>> multiply('a',3)
    'aaa'

    """
    return a * b

if __name__ == '__main__':
    doctest.testmod(verbose=True)