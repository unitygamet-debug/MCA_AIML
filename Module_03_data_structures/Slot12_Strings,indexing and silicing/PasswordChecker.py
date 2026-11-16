users = {}
h=0
p=0
l=0
a=0
n=0
while h!=1:
    username = input("Enter username: ")
    password = input("Enter password: ")
    for i in password:
        if i in "@#$%&*!":
            p=p+1
        if len(password) >= 8:
            l=l+1
        if i.isalpha():
            a+=1
        if i.islower():
            n+=1


    if p>0 and l>0 and a>0 and n>0:
        users[username] = password
    else:
      print("Password must have at least 8 characters and special characters, Please re-enter:")


    h=int(input("if You want to cancel  Username and password entry then enter '1' to cancel:"))






username = input("Enter username without space or Special characters: ")

if username in users:

    count = 0

    while count < 5:

        password = input("Enter password: ")

        if password == users[username]:

            print("Access granted")


            if len(password) >= 8:


                alphabet = False

                for ch in password:
                    if ch.isalpha():
                        alphabet = True


                special = False

                for ch in password:
                    if ch in "@#$%&*!":
                        special = True

                if alphabet and special:
                    print("Password is valid")
                    break

                else:
                    print("Password must have alphabet and special character")

            else:
                print("Password must have at least 8 characters")

        else:
            print("Wrong password")
            count = count + 1

    if count == 5:
        print("You used all 5 attempts")

else:
    print("Username not found")