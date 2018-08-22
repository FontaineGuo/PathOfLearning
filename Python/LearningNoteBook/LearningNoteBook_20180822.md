## 2018.08.22

#### How getattr works
```
class handler:
    def handle(self, name):
        meth = getattr(self, name, None)
        print(meth)

class fun(handler):
    def sub_fun_one(self):
        print("Fuck 1")

class fun2(handler):
    def sub_fun_two(self):
        print("Fuck 2")



h1 = fun()
h1.handle('sub_fun_one')
h2 = fun2()
h2.handle('sub_fun_two')
```
result
```
<bound method fun.sub_fun_one of <__main__.fun object at 0x0000019CD2834048>>
<bound method fun2.sub_fun_two of <__main__.fun2 object at 0x0000019CD28340B8>>

```

#### Chapter 25 Q&A
```
https://stackoverflow.com/questions/24928908/python3-type-str-doesnt-support-the-buffer-api

```