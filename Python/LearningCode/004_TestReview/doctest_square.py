def square(x):
    '''
    Squares a number and return the reslut.
    
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x**2

if __name__ == '__main__':
    import doctest, doctest_square
    doctest.testmod(doctest_square)