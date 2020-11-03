#Login prompt screen
def login():
    system = input("Are you a new user? (y/n) ")
    if system.lower() == "y":
        newUser()
    elif system.lower() == "n":
        oldUser()

#Make new user and password
def newUser():
    print("***Create new user***")
    while():
        username = input("Please give a username: ")
        if validUsername == False:
            print("Invalid username!")
            continue

        password = input("Please give a password: ")
        if validPassword == False:
            print("Invalid password")
            continue
        break

    writeToFile(username,password)

#Login with excisting username and password
def oldUser():
    print("Login with excisting username and password:")
    username = input("Username: ")
    password = input("Password: ")
    checkUser(username,password)
    
def validUsername(username):
    pass

def validPassword(password):
    pass

#add new user and password to database
def writeToFile(username,password):
    a_file = open("users.txt", "a")
    a_file.write(f"{username}:{password}")
    a_file.close()

#check username and password from database
def checkUser(username,password):
    user_list = readFromFile()
    isMatch = False
    for item in user_list:
        userdata = item.split(":")
        if username == userdata[0] and password == userdata[1]: #Case sensitive
            accessData()
            isMatch = True

    if isMatch == False:
        print("Username and password not found or did not match")

#Read information from file. Creates a list of users and passwords (NOT SO SAFE!)
def readFromFile():
    new_list = []
    a_file = open("users.txt","r")
    for line in a_file:
        stripped_line = line.strip()
        new_list.append(stripped_line)
    a_file.close()
    return new_list

#Access secret information
def accessData():
    a_file = open("accessFile.txt", "r")
    for line in a_file:
        print(line)
    a_file.close()


def main():
    print("***Welcome to Jefishub login system***")
    login()
    pass

"""MAIN FUNCTION -> starts the game"""
if __name__ == "__main__":
    main()