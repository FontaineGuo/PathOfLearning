# 2018.7.16

## Chapter 1

#### Single-Quoted Strings and Escaping Quotes

```
>>>'Hello world!'
'Hello world!'

>>>'"hello world", she said'
'"hello world", she said'
```

#### Long string
```
print(```This is a very long string, It continues here.
And it's not over yet. "hello world!"
Still here```)
```

#### Raw string
```
>>> path = 'C:\nowhere'
>>> path
'C:\nowhere'

>>> print('C:\\nowhere')
C:\nowhere

>>> print(r'C:\nowhere')
C:\nowhere

>>>print(r"This is illegal\")
SyntaxError :EOL while scanning string literal
```

#### String Encode
```
>>> "Hello world!".encode("ASCII")
>>> "Hello world!".encode("UTF-8")
>>> "Hello world!".encode("UTF-32")
```

#### Get help
```
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']



>>>help(sum)
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)   
      
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers      When the iterable is empty, return the start value.    
      
    This function is intended specifically for use with numeric values and may    reject non-numeric types.



>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

#### write a help doc
```
# coding=utf-8
 
"""
This is module help. 
"""
 
class C1(object):
    """
    class's help string.
    """
    def __init__(self, a):
        """
        method's help string.
 
        """
        pass
 
 
def f1():
    """
    this is f1's help string.
 
    """
    pass
```

## Chapter 2
#### shortcut of list
```
>>> numbers = [1,2,3,4,5,6,7,8,9,10]
>>> numbers[-3:-1]
[8,9,10] 

>>> numbers[:3]
[1,2,3]

>>> numbers[:]
[1,2,3,4,5,6,7,8,9,10]
```
#### step of list
```
>>> numbers = [1,2,3,4,5,6,7,8,9,10]
>>> numbers[0:10:2]
[1,3,5,7]

>>> numbers[::4]
[1,5,9]
```

#### Mutiplication
```
[42]*4
[42, 42, 42, 42]
```
