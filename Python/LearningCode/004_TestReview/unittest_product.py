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