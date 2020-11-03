"""
# Step 1 - Import the unittest module in your program

import unittest

# Step 2 - Define a function to be tested.
# In the following example, add() function is to be subjected to test.

def add(x,y):
    return x+y

# Step 3 - Create a testcaste by subclassing unittest.TestCase

class SimpleTest(unittest.TestCase):
    # Step 4 - Defince a test as a methon inside the class
    # Name of method must start with 'test'.

    def test_add1(self):
        # Step 5 - assertEquals() function compares
        # result of add() function with arg2 arguments
        # and throws assertionError if comparison fails.
        self.assertEqual(add(4,5),9)

# Step 6 -  Finally, call main() method from the unittest module.

if __name__ == '__main__':
    unittest.main()
"""

import unittest
def add(x,y):
    return x + y
class SimpleTest(unittest.TestCase):
    def testadd1(self):
        self.assertEquals(add(4,5),9)
if __name__ == '__main__':
    unittest.main()