def login():
    system = input("Are you a new user? (y/n) ")
    if system.lower() == "y":
        newUser()
    elif system.lower() == "n":
        oldUser()

def newUser():
    username = input("Please give a username: ")
    password = input("Please give a password: ")
    pass

def oldUser():
    username = input("Please give your username: ")
    password = input("Please give your password: ")
    pass

def writeToFile(username,password):
    pass

def readFromFile(filename):
    pass

def main():
    print("***Welcome to Jefishub login system***")
    login()
    pass

"""MAIN FUNCTION -> starts the game"""
if __name__ == "__main__":
    main()