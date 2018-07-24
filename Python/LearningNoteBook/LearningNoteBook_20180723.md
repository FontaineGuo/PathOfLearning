## Chapter 9

#### Constructors
```
class FooBar:
    def __init__(self):
        self.somevar = 42
>>> f = FooBar()
>>> f.somevar
42



# optional parameter
class FooBar:
    def __init__(self, value = 42):
        self.somevar = value

>>> f = FooBar('This is a constructor argument')
>>> f.somevar
'This is a constructor argument'
```

#### Overriding Methods
```
class A:
    def hello(self):
        print("Hello. I'm A")

class B(A):
    def hello(self):
        print("Hello, I'm B")
```

#### using super Function
```
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Ahaaa ...')
            self.hungry = False
        else:
            print('No, thanks')

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.soud = 'Squawk!'
    def sing(self):
        print(self.sound)
```


#### The Basic Sequence and Mapping Protocol
```
__len__(self)
__getitem__(self, key)
__setitem__(self, key, value)
__delitem__(self, key)
```

#### The property Function
```
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)
```
now you could treat width height size as the same way
```
>>> r = Rectangle()
>>> r.width = 10
>>> r.height = 5
>>> r.size
(10, 5)
>>> r.size = 150, 100
>>> r.width
150
```

#### Static Methods and Class Methods
作者：fosmjo
链接：https://www.zhihu.com/question/20021164/answer/42704772
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
@classmethod means: when this method is called, we pass the class as the first argument instead of the instance of that class (as we normally do with methods). This means you can use the class and its properties inside that method rather than a particular instance.
```
```
@staticmethod means: when this method is called, we don't pass an instance of the class to it (as we normally do with methods). This means you can put a function inside a class but you can't access the instance of that class (this is useful when your method does not use the instance).
```

```
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    
    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)
```

p.s
```
classmethod 可以用来创造特殊的构造函数，以弥补python没有overwritting的概念

staticmethod 可以在不实例化类的时候调用函数，以获得更好的封装性
```

#### __getattr___, ___setattr___, and Friends
```
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else: #in case of called setattr again with wrong attr
            self.__dict__[name] = value
    def __getattr__(self, name):
        if name = 'size':
            return self.width, self.height
        else:
            raise AttributeError()
```

#### itrator
```
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    
    def __iter__(self):
        return self

>>> fibs = Fibs()

for f in fibs:
    if f > 1000:
        printf(f)
        break
>>> 1579
```

#### itrator could convert to a sequence
```
ti =  TestIterator()
list(ti)
```