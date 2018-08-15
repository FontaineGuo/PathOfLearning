## Chapter 14

#### Summary

+ socket module
+ urllib\urllib3
+ SocketServer
+ select\poll
+ Twisted




#### P.S  three way to escape backslashes
```
# use '/' instead of '\'
（‘d:/77/111.txt’）

# use r to avoid escape
（r‘d:\77\111.txt’）

# use '\\'
‘d:\\77\\111.txt
```

## Chapter 15

#### Python Web Application Frameworks

Name | Web Site
:--- | ---
Django | https://djangoproject.com
TurboGeear | http://www.turbogears.org
web2py | http://www.web2py.com
Grok | http://grok.zope.org
Zope2 | http://www.zope.org/en/latest/
Pyramid | https://trypyramid.com

## Chapter 16

#### Test Code
```
from area import rect_area
height = 3
width = 4
correct_answer = 12
answer = rect_area(height, width)
if anwser == correct_answer:
    print('Test passed')
else:
    print('Test failed')
```

#### test-driven development process
1.Figure out the new feature you want.

2.Write some skeleton code for the feature so that your program runs without any syntax errors

3.Write dummy code for your skeleton, just to appease the test

4.Rewrite (or refactor) the code so that it actually does what it's supposed to.



#### test tools
+ unittest
```
import unittest, product

class ProductTestCase(unittest.TestCase):
    def testIngegers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = product.product(x, y)
                self.failUnless(p == x*y, 'Integer multip;ication failed')

    def testFloats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x/10.0
                y = y/10.0
                p = product.product(x, y)
                self.failUnless(p == x*y, 'Float multip;ication failed')

if __name__ == '__main__':unittest.main()
```
```
$ python unittest_product.py
Ran 2 tests in 0.017s

OK
```

+ doctest
```
def square(x):
    '''
    Squares a number and return the reslut.
    
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x**2
```
```
$ python doctest_square.py -v
-----------
Trying:
    square(2)
Expecting:
    4
ok
Trying:
    square(3)
Expecting:
    9
ok
1 items had no tests:
    doctest_square
1 items passed all tests:
   2 tests in doctest_square.square
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
------------
```


