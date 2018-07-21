## Chapter 7

#### The magic of Objects
+ Polymorphism : you can use the same operations objects of different classes, and they will work as if 'by magic'

+ Encapsulation : You hide unimportant details of how objects work form the outside world

+ Inheritance: You can create speciallized classes of objects from general ones


#### Class

+ Privacy Revisited
```
class Secretive:
    def __inaccessible(self):
        print('Bet you can't see me ...')

    def accessible(self):
        print('The secret msg is:')
        self.__inaccessible()
```
access them
```
>>> s = Secretive()

>>> s.accessible()
>>> s.__Secretive__inaccessible()
```

+ Superclass
```
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, seq):
        return seq
class SPAMFilter(Filter):
    def init(self): #SPAMFilter is a subclass of Filter
        self.blocked = ['SPAM']
```
 + investigating Inheritance
```
>>> issubclass(SPAMFilter, Filter)
True
```
