## Chaper 5

#### Printing Multiple Arguments
```
>>>print('I', 'love', 'you', sep='_')
I_love_you
```

#### Assignment Magic
```
>>> x,y,z = 1,2,3
>>> print(x,y,z)
1 2 3

#chage value of var
>>> x = 1
>>> y = 2
x,y = y,x
>>> print(x,y)
2 1

>>> a, b, *rest = [1,2,3,4]
>>> rest
[3,4]
```

#### The follow values are regared by interperter as false
```
False None 0 "" () [] {}
```

#### The python comparison operators
operatot|Description
---|:--:|
x is y  |   x and y are the same object|
x is not y | x and y are different objects
x in y | x is member in y
x not in y | x is not member in y

#### Assertuibs
```
>>> age = -1
>>> assert 0<age<100, 'The var is wrong'
AssertionError: The var is wrong
```

#### Parallel Iteration
```
names = ['Anna', 'Fontaine']
ages = ['21', '22']

for name, age in zip(names, ages):
    print(name, age)
>>>
Anna 21
Fontaine 22
```

#### And three for the road
pass
```
if name == 'Fontaine Guo'
    print('Welcome!')
elif name == 'Shroud'
    pass
```

#### exec and eval
exec
```
>>> from math import sqrt
>>> scope = {}
>>> exec('sqrt = 1', scope)
>>> sqrt(4)
2.0
>>> scope['sqrt']
1
```

eval
```
>>> scope = {}
>>> scope['x']=2
>>> scope['y']=3
>>> eval('x*y', scope)
6
```

## Chapter6

#### funcation
+ Documenting Functions
```
def main():
    help(square)

def square(x):
    'Calculated the square of the number x'
    return x*x

if __name__ == '__main__':
    main()
    
output:
    square(x)
        Calculated the square of the number x
```
+ Keyword Parameters and Defaults
```
def rotate(Angle, Extra)
    print('Angle:', Angle, "Extra:", Extra)

>>> roatate(Angle=20, Extra=30)
```
p.s use keyword to avoid misleading

+ Collecting Parameters
```
def print_params(*params):
    print(params)

# send a tuple
>>> params = (1,2)
>>> add(*params)
3

# send a dic
>>> params = {'name':'Sir Robin', 'greeting':'Well met'}
>>> hello_3(**params)

```

+ Scoping
```
>>> x = 1
>>> x
1
>>> scope = vars()
>>> scope['x']
1
```

+ Global
```
>>> x = 1
>>> def change():
...  global x
...  x = x+1
...
>>> x
1
>>> change()
>>> x
2
```

+ nested scopes == closure(闭包)
```
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor
>>> double = multiplier(2)
>>> double(5)
10
```