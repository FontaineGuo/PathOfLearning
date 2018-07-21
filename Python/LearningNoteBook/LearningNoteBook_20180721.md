## Chpater 8

 #### Exception
 ```
 >>> raise Exception
 ```

 #### Custom Exception Class
 ```
 class SomeCustomException(Exception): pass
 ```

 #### catch exception class
 ```
 try：
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero !")
 ```

 + p.s eval
 ```
 def calc(self , expr):
    return eval(expr)

calc('10/2')
 ```

 #### catch Two exception with one block
 ```
  try：
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, TypeError, NameError):
    print("Your numbers were bogus")
 ```

 #### catch the object
 ```
 except (ZeroDivisionError, TypeError, NameError) as e:
    print(e)
 ```

 #### And finally
 ```
 x = None
 try:
    x = 1/0
finally:
    print('Cleaning up...')
    del x
 ```

 #### Not All that Exceptional
 + warning
 ```
 >>> from warnings import warn
>>> warn("I've got a bad feeling about this")
__main__:1: UserWarning: I've got a bad feeling about this
 ```