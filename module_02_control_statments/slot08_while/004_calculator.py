#ask from user for include if add how many no u want to add after if choice
'''while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Quit")
choice = input("choose:")'''
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Choose: ")

    if choice == "1":
        n = int(input("How many numbers do you want to add? "))
        total = 0
        count = 1

        while count <= n:
            num = int(input("Enter number: "))
            total = total + num
            count = count + 1

        print("Addition =", total)

    elif choice == "2":
        n = int(input("How many numbers do you want to subtract? "))
        result = int(input("Enter first number: "))
        count = 1

        while count < n:
            num = int(input("Enter number: "))
            result = result - num
            count = count + 1

        print("Subtraction =", result)

    elif choice == "3":
        n = int(input("How many numbers do you want to multiply? "))
        result = 1
        count = 1

        while count <= n:
            num = int(input("Enter number: "))
            result = result * num
            count = count + 1

        print("Multiplication =", result)

    elif choice == "4":
        n = int(input("How many numbers do you want to divide? "))
        result = float(input("Enter first number: "))
        count = 1

        while count < n:
            num = float(input("Enter number: "))
            result = result / num
            count = count + 1

        print("Division =", result)

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice")
