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
import login
import random
import string
import os

class SimpleTest(unittest.TestCase):
    #Username, testing with any letters with length 3-50
    def test_username1(self):
        for i in range(100):
            name = ""
            name_length = random.randint(3,50)
            for i in range(name_length):
                name += random.choice(string.ascii_letters)
            self.assertEqual(login.validUsername(name),True)

    #Username, testing specific names
    def test_username2(self):
        test_names = [" ", "1Jukka","Jukka1", "Juk1ka", " Jukka", "Ju kka", "Jukka ", ",Jukka"]
        for test_name in test_names:
            name = test_name
            self.assertEqual(login.validUsername(name),False)

    #Password, testing with any combination of letters and numbers, length 7-50
    def test_password1(self):
        for i in range(100):
            name = ""
            name_length = random.randint(7,50)
            for j in range(name_length):
                name += ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(name_length))
            self.assertEqual(login.validPassword(name),True)

    #Password, testing specific words
    def test_Password2(self):
        test_names = [" ", "1","Ju", "Juk1ka ", " Jukka", "Ju kka", "Ju-kka" ",Jukka"]
        for test_name in test_names:
            name = test_name
            self.assertEqual(login.validPassword(name),False)


    #Testing readFromFile functionality
    def test_readFile(self):
        test_file = open("testfile1.txt", "w")
        test_file.write("Jukka:salasana\nPekka:password\nJaakko:pw123")
        test_file.close()
        self.assertEqual(login.readFromFile("testfile1.txt"),["Jukka:salasana","Pekka:password","Jaakko:pw123"])
        os.remove("testfile1.txt")

    #Testing accessData functionality
    def test_accessData(self):
        test_file = open("testfile2.txt", "w")
        test_file.write("Secret text")
        test_file.close()
        self.assertEqual(login.accessData("testfile2.txt"),"Secret text")
        os.remove("testfile2.txt")       

    #Testing checkUser functionality
    def test_checkUser(self):
        test_file = open("testfile3.txt", "w")
        test_file.write("Jukka:salasana1\nPekka:password2")
        test_file.close()
        self.assertEqual(login.checkUser("Jukka","salasana1","testfile3.txt"),True)
        self.assertEqual(login.checkUser("Pekka","password2", "testfile3.txt"),True)
        self.assertEqual(login.checkUser("Jere","password1", "testfile3.txt"),False)
        os.remove("testfile3.txt") 
    


if __name__ == '__main__':
    unittest.main()