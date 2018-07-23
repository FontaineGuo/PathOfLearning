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


