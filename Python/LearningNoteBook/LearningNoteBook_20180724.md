## Continue Chapter 9

#### Generator
```
nested = [[1,2],[3,4],[5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

>>> for num in flatten(nested):
        print(num)
1
2
3
4
5
```

#### Loopy generator
```
>>> g = ((i+2)**2 for i in range(2,27))
>>> next(g)
16
```

#### recursive generator
```
# try cluase for string-like object
def flatten(nested):
    try:
        # Don't iterate over string-like object:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

```