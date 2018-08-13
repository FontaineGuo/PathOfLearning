## Chapter 10

#### modules
```
>>> import math
>>> math.sin(0)
0.0
```
#### reload
```
Cause module may have different behavior can import each other, when import module
,interpreter only execute module for once
if want run them again, use reload
```
```
>>> import importlib
>>> hello = importlib.reload(hello)
Hello, world !
```

#### Addomg Test Code in a Module
```
# hello3.py
def hello()
    print('Hello World')
# A test:
hello()
```

#### how to create a package
File/Directory|Description
:---|:--:
~/Python/ | Directory in PYTHONPATH
~/Python/drawing/ | Package directory
~/Python/drawing/__init__.py | Package code
~/Python/drawing/colors.py | colors module
~/Python/drawing/shapes.py | shapes moduel

#### use package
```
import drawing
import drawing.colors
from drawing import shapes
```

### data structure
#### Heap Deques
Heap
```
from heapq import *
```
for example:
```
from heapq import *
>>> heap
[0,1,3,6,2,8,4,7,9,5]
>>> heappush(heap, 0.5)
>>> heap
[0,0.5,3,6,1,8,4,7,9,5,2]

# the num in position i are always greater than num in position i/2
```

## Chapter 11
####  Files and Stuff
Value | Description
:---|:---
r | read mode
w | write mode
x | Exclusive write mode
a | Append mode
b | Binary mode
t | Text mode
+ | Read/write mode

#### examples
```
>>> f = open('somefile.txt', 'w')
>>> f.write('hello')
>>> f.close()

>>> f = open('somefile.txt', 'w')
>>> f.read(5)
hello

# readline/writeline
>>> f = open('somefile.txt', 'w')
>>> lines = f.readlines()
>>> f.close()
>>> lines[1] = "isn't a\n"
>>> f = open('somefile.txt', 'w')
>>> f.writelines(lines)
>>> f.close()
```



#### Piping Output
```
$ cat somefile.txt | python somescript.py | sort
```

#### Lazy line iteration with fileinput
```
import fileinput
for line in fileinput.input(filename):
    process(line)
```

#### File Iterators
```
with open(filename) as f:
    for line in f:
        process(line)
```

