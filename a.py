import os.path

def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()
        def appendNew():
            file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    username = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(username)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close
    
    def readPasswords():
        file = open('info.txt', 'r')
        content = file.read()
        file.close()
    print(content)