# 2018.07.18
## Chapter 2

#### "in" operator
```
>>> sen = "Hi, Walker"
>>> 'W' in sen
True
>>> 'Q' in sen
False
```

#### Sequence membership test
```
# Check a user name and PIN code

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

 
username = input('user name: ')
pin = input('PIN code: ')

if [username, pin] in database: print('Acess granted')
```

#### some method
```
len()
min()
max()
```

### The list Funcation

#### basic funcation
```
>>>list("Hello")
['H','e','l','l','o']
```

#### delete elements and assign
```
# delete
>>> names = ['Jack', 'Fontaine', 'Earl', 'Dee-Dee']
>>> del names[2]
>>> names
['Jack', 'Fontaine', 'Dee-Dee']

# assign
>>> name = list('Perl')
>>> name[2:] = list('ar')
>>> name
['P', 'e', 'r', 'l']

# assign for inserting a num
>>> number = [1,5]
>>> number[1:1] = [2,3,4]
>>> number
[1,2,3,4,5]
```

#### extend
```
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a.extend(b)
```

#### index 
```
>>> names = ['Jack', 'Fontaine', 'Earl', 'Dee-Dee']
>>> names.index('Jack')
0
```

#### pop
```
>>> x = [1,2,3]
>>> x.pop()
3
```

#### reverse
```
>>> x = [1,2,3]
>>> x.reverse()
>>> x
[3,2,1]
```

### Tuples

Tuples are almost the same as list but there is only difference is that tuples cant be changed
```
>>> 1, 2, 3
(1,2,3)

# if there are only one value, write like this
>>> 22
(22, )

# convert a list to tuple
>>> tuple([1,2,3])
(1,2,3)
>>> tuple('abc')
('a', 'b', 'c')
```

## Chapter 3

#### string format
```
# method one
>>> format = 'Hello, %s, %s enough for ya?'
>>> valuse = ('world', hot)

# method two
>>> from string import Template
>>> tmpl = Template("Hello $w")
>>> tmpl.substitute(who="World")
'Hello world'

# method three
>>> "{0}, {1},and {2}".format("first", "second", "third")
'first, second and third'
```

#### string format long version
```
>>> "{{stay with me}}".format
>>> {stay with me}

>>> fullname = ['Alfred', 'Fisher']
>>> "Mr {name[1]}".format(name=fullname)
"Mr Smoketoomuch"

>>> import math
>>> tmpl = "The {mod.__name__} module defines the value pi"
>>> tmpl.format(mod=math)
'The math module defines the value pi'
```

#### signs, alignment and Zero-padding
```
>>> "{:$^15}".format("WIN BIG")
'$$$ WIN BIG $$$'

# flag, 
# 0 means zero-padded
>>> '{:010.2f}'.format(pi)
'0000003.13'
# < left, > right, ^ centered
>>> print('{:<010.2f}\n{:^010.2f}\n{:>010.2f}')
3.14
   3.14
      3.14
```