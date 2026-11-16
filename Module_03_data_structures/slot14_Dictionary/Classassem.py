print("-------- SECURE EMPLOYEE ACCOUNT SYSTEM ----------")

accounts = {}

# Number of accounts
n = abs(int(input("Enter number(+ve) of accounts to create  ")))


# Create accounts
for i in range(n):

    print("\n--- Account", i + 1, "---")

    username = input("Enter username: ")

    while True:

        password = input("Enter password: ")

        # Check password
        upper = False
        lower = False
        digit = False
        special = False
        space = False

        # Check every character
        for ch in password:
            if ch == " ":
                space = True

            if ch.isupper():
                upper = True

            if ch.islower():
                lower = True

            if ch.isdigit():
                digit = True

            if ch in "@#$%!":
                special = True



        # Check all conditions
        if len(password) < 8:
            print("Password must contain at least 8 characters.")

        elif upper == False:
            print("Password must contain an uppercase letter.")

        elif lower == False:
            print("Password must contain a lowercase letter.")

        elif digit == False:
            print("Password must contain a digit.")

        elif special == False:
            print("Password must contain a special character.")

        elif space == True:
            print("Password must not contain a space.")

        else:
            # Password is correct
            break

        print("Please enter the password again.")

    # Confirm password
    while True:

        confirm = input("Confirm password: ")

        if password == confirm:
            print("Account created successfully!")
            break
        else:
            print("Passwords do not match.")

    # Store account
    accounts[username] = password




print("\n===== EMPLOYEE LOGIN =====")

attempts = 0

while attempts < 5:

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in accounts:

        if accounts[username] == password:
            print("Login successful!")
            print("Welcome", username)
            break

        else:
            print("Invalid username or password.")

    else:
        print("Invalid username or password.")

    attempts = attempts + 1

    print("Attempts remaining:", 5 - attempts)

else:
    print("Access Denied!")
    print("Maximum login attempts exceeded.")