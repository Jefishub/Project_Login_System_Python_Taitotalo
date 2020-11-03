#Login prompt screen
def loginScreen():
    while True:
        system = input("Login as excisting user (y/n) ? ")
        if system.lower() == "n":
            newUser()
            break
        elif system.lower() == "y":
            oldUser()
            break
        else:
            print("Invalid command")
            continue



#Make new user and password
def newUser():
    """ Function for creating new user. Asks for a new username and password. 
        Checks if inputs are valid and if yes, then writes them to users.txt file via writeToFile function
    """
    print("***Create new user***")
    while True:
        username = input("Please give a username: ")
        if validUsername(username) == False:
            print("Invalid username! Only letters are allowed, minimum of 3 letters long")
            continue

        password = input("Please give a password: ")
        if validPassword(password) == False:
            print("Invalid password. Only letters and numbers are allowed, minimum of 7 characters")
            continue

        writeToFile(username,password)        
        break



#for now, only letters allowed (case sensitive).
def validUsername(username):
    if username.isalpha() and len(username) > 2:
        return True
    else:
        return False



#for now, only letters and numbers allowed (Case sensitive)
def validPassword(password):
    if password.isalnum() and len(password) > 6:
        return True
    else:
        return False



#Delete user functionability (Only for Admin)
def deleteUser(username):
    """Function that removes a user from database (users.txt file)
       This function only works when logged in as Admin

    Args:
        username (String): The username to be deleted
    """
    user_list = readFromFile()
    #remove user from user_list
    for i in range(len(user_list)):
        userdata = user_list[i].split(":")
        if username == userdata[0]:
            user_list.pop(i)
            break
    #overwrite users.txt with updated user_list
    a_file = open("users.txt", "w")
    for i in range(len(user_list)):
        if i < len(user_list) - 1:
            a_file.write(user_list[i] + "\n")    #Adds new row to users.txt file 
        else:
            a_file.write(user_list[i])          #No new row added to users.txt file
    a_file.close()



#add new user and password to database
def writeToFile(username,password,user_file="users.txt"):
    a_file = open(user_file, "a")
    a_file.write(f"\n{username}:{password}")
    a_file.close()



#Login with excisting username and password
def oldUser():
    print("Login with excisting username and password:")
    username = input("Username: ")
    password = input("Password: ")
    if checkUser(username,password):
        loggedInScreen(username)
    else:
        print("Username and password did not excist or match")



#check username and password from database
def checkUser(username,password):
    user_list = readFromFile()
    isMatch = False
    for item in user_list:
        userdata = item.split(":")
        if username == userdata[0] and password == userdata[1]: #Case sensitive
            isMatch = True
    return isMatch


#Logged in screen gives ability to give commands when username and password matched
def loggedInScreen(user):
    """loggedInScreen gives the user command options. When logged as user only commands are 'read' and 'exit'.
       When logged in as Admin, adds 'delete' command for use

    Args:
        user (string): The name of the currently logged in user
    """
    while True:
        #ADMIN ACCESS ONLY -> delete user possibility
        if user == "Admin":
            command = input("Read file (read), delete user(del), exit (exit): ")
            #command action for del
            if command == "del":
                del_user = input("Give username: ")
                deleteUser(del_user)

        #User access command      
        else:
            command = input("Read file (read), exit (exit): ")

        #command actions
        if command == "read":
            accessData()
            continue
        elif command == "exit":
            break




#Read information from file. Creates a list of users and passwords (NOT SO SAFE!)
def readFromFile(user_file="users.txt"):
    new_list = []
    a_file = open(user_file,"r")
    for line in a_file:
        stripped_line = line.strip()
        new_list.append(stripped_line)
    a_file.close()
    return new_list



#Access secret information
def accessData(hidden_file="accessFile.txt"):
    a_file = open(hidden_file, "r")
    for line in a_file:
        print(line)
    a_file.close()



def main():
    while True:
        print("***Welcome to Jefishub login system***")
        loginScreen()
        new_game = input("Do you want to play again? (y/n)")
        if new_game == "y":
            continue
        else:
            break
    



"""MAIN FUNCTION -> starts the game"""
if __name__ == "__main__":
    main()