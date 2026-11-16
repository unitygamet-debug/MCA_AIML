SPECIAL_CHARACTERS = "@#$%!&*^_-+=~?/.,:;|"
accounts = {}

print("===== EMPLOYEE ACCOUNT SYSTEM =====")

while True:
    try:
        num_accounts = int(input("Enter number of accounts to create: "))
        if num_accounts <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

for i in range(1, num_accounts + 1):
    print(f"\n--- Account {i} ---")

    username = input("Enter username: ")

    # ---------------- Stage 2: Secure Password Creation ----------------

    while True:
        password = input("Enter password: ")

        errors = []

        if len(password) < 8:
            errors.append("Password must contain at least 8 characters.")

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        has_space = False

        for ch in password:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
            elif ch == " ":
                has_space = True
            elif ch in SPECIAL_CHARACTERS:
                has_special = True

        if not has_upper:
            errors.append("Password must contain at least one uppercase alphabet.")
        if not has_lower:
            errors.append("Password must contain at least one lowercase alphabet.")
        if not has_digit:
            errors.append("Password must contain at least one digit.")
        if not has_special:
            errors.append("Password must contain at least one special character (e.g. @ # $ % !).")
        if has_space:
            errors.append("Password must not contain any spaces.")

        if not errors:
            break

        print("Password rejected!")
        for error in errors:
            print(error)
        print("Please enter the password again.")

    # Confirm password
    while True:
        confirm_password = input("Confirm password: ")
        if confirm_password == password:
            accounts[username] = password
            print("Account created successfully!")
            break
        else:
            print("Passwords do not match. Please enter the confirm password again.")

# ---------------- Stage 3: Employee Login ----------------

print("\n===== EMPLOYEE LOGIN =====")

max_attempts = 5
attempts = 0
logged_in = False

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in accounts and accounts[username] == password:
        print(f"Login successful! Welcome {username}")
        logged_in = True
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Invalid username or password. Attempts remaining: {remaining}")
        else:
            print("Access Denied! Maximum login attempts exceeded.")