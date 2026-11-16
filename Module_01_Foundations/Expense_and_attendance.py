# Expense, Attendance, Grading and Billing Manager  (Very Simple Version)
# Uses only basic Python: variables, if/else, loops, lists, dictionaries, functions.
# Run with:  python basic_main.py

# ---------------- SETTINGS (you can change these) ----------------
CATEGORIES = ["Food", "Travel", "Utilities", "Stationery", "Other"]
SUBJECTS = ["Maths", "Science", "English", "History", "Computer"]
PASS_MARK = 35
TAX_RATE = 0.18

# ---------------- DATA (lists keep our records) ----------------
expenses = []
people = []
students = []
bills = []
working_days = [0]      # a list, so functions can change it


# ---------------- CHECKING NUMBERS ----------------
def is_number(text):
    """True if text looks like a positive number such as 45 or 250.50"""
    if text.count(".") > 1:
        return False
    return text.replace(".", "").isdigit() and text.isascii()


def get_int(prompt, min_val, max_val, message):
    """Keep asking until the user types a whole number in range."""
    while True:
        text = input(prompt).strip()
        if text.isdigit() and text.isascii():
            value = int(text)
            if value >= min_val and value <= max_val:
                return value
        print(message)


def get_float(prompt, message, min_val, max_val, can_equal_min):
    """Keep asking until the user types a number in range."""
    while True:
        text = input(prompt).strip()
        if is_number(text):
            value = float(text)
            if value <= max_val:
                if value > min_val:
                    return value
                if value == min_val and can_equal_min:
                    return value
        print(message)


def get_name(prompt):
    """Name must be 2 to 40 letters (spaces allowed)."""
    while True:
        name = input(prompt).strip()
        if len(name) >= 2 and len(name) <= 40 and name.replace(" ", "").isalpha():
            return name
        print("Name must contain 2-40 letters.")


def get_text(prompt, message):
    """Text must not be empty."""
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print(message)


def get_category():
    """User must type one of the categories."""
    while True:
        answer = input("Category (Food/Travel/Utilities/Stationery/Other): ").strip().lower()
        for category in CATEGORIES:
            if answer == category.lower():
                return category
        print("Choose a category from the list.")


# ---------------- EXPENSE MODULE ----------------
def add_expense():
    description = get_text("Description: ", "Description cannot be empty.")
    category = get_category()
    amount = get_float("Amount: ", "Amount must be a positive number.", 0, 1000000, False)
    expense = {"description": description, "category": category, "amount": round(amount, 2)}
    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No records available.")
        return
    print("Description          Category        Amount")
    print("---------------------------------------------")
    for e in expenses:
        print(f"{e['description']:<20} {e['category']:<12} {e['amount']:>10.2f}")


def expense_summary():
    if len(expenses) == 0:
        print("No records available.")
        return
    grand_total = 0
    print("CATEGORY        TOTAL")
    for category in CATEGORIES:
        category_total = 0
        for e in expenses:
            if e["category"] == category:
                category_total = category_total + e["amount"]
        if category_total > 0:
            print(f"{category:<12} {category_total:>10.2f}")
            grand_total = grand_total + category_total
    print("-----------------------")
    print(f"{'GRAND TOTAL':<12} {grand_total:>10.2f}")

    highest = expenses[0]
    lowest = expenses[0]
    for e in expenses:
        if e["amount"] > highest["amount"]:
            highest = e
        if e["amount"] < lowest["amount"]:
            lowest = e
    print("Highest expense:", highest["description"], "-", highest["amount"])
    print("Lowest expense :", lowest["description"], "-", lowest["amount"])


def expense_menu():
    while True:
        print("\n--- EXPENSE MANAGEMENT ---")
        print(" 1. Add Expense")
        print(" 2. View All Expenses")
        print(" 3. Expense Summary")
        print(" 4. Back")
        choice = get_int("Enter your choice (1-4): ", 1, 4, "Invalid choice. Enter 1-4.")
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            expense_summary()
        else:
            return


# ---------------- ATTENDANCE MODULE ----------------
def attendance_status(percent):
    if percent >= 75:
        return "Eligible"
    elif percent >= 60:
        return "Warning"
    else:
        return "Shortage"


def set_working_days():
    working_days[0] = get_int("Total working days: ", 1, 1000,
                              "Enter a whole number of at least 1.")


def add_person():
    if working_days[0] == 0:
        set_working_days()
    total = working_days[0]
    name = get_name("Name: ")
    person_id = get_text("ID: ", "ID cannot be empty.")
    present = get_int("Days present: ", 0, total,
                      "Days present must be between 0 and " + str(total) + ".")
    percent = present / total * 100
    status = attendance_status(percent)
    person = {"name": name, "id": person_id, "total": total,
              "present": present, "percent": percent, "status": status}
    people.append(person)
    print(f"Added {name}: {percent:.2f}% - {status}")


def view_attendance():
    if len(people) == 0:
        print("No records available.")
        return
    print("Name                 Total  Present  Attendance %  Status")
    print("--------------------------------------------------------")
    for p in people:
        print(f"{p['name']:<20} {p['total']:>5} {p['present']:>8} {p['percent']:>12.2f}  {p['status']}")


def attendance_summary():
    if len(people) == 0:
        print("No records available.")
        return
    sum_percent = 0
    eligible = 0
    warning = 0
    shortage = 0
    highest = people[0]
    lowest = people[0]
    for p in people:
        sum_percent = sum_percent + p["percent"]
        if p["status"] == "Eligible":
            eligible = eligible + 1
        elif p["status"] == "Warning":
            warning = warning + 1
        else:
            shortage = shortage + 1
        if p["percent"] > highest["percent"]:
            highest = p
        if p["percent"] < lowest["percent"]:
            lowest = p
    print("Total students     :", len(people))
    print(f"Average attendance : {sum_percent / len(people):.2f}%")
    print(f"Highest            : {highest['name']} ({highest['percent']:.2f}%)")
    print(f"Lowest             : {lowest['name']} ({lowest['percent']:.2f}%)")
    print("Eligible:", eligible, "| Warning:", warning, "| Shortage:", shortage)


def attendance_menu():
    while True:
        print("\n--- ATTENDANCE MANAGEMENT ---")
        print(" 1. Set Total Working Days")
        print(" 2. Add Person")
        print(" 3. View Attendance")
        print(" 4. Attendance Summary")
        print(" 5. Back")
        choice = get_int("Enter your choice (1-5): ", 1, 5, "Invalid choice. Enter 1-5.")
        if choice == 1:
            set_working_days()
        elif choice == 2:
            add_person()
        elif choice == 3:
            view_attendance()
        elif choice == 4:
            attendance_summary()
        else:
            return


# ---------------- GRADING MODULE ----------------
def get_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    elif percent >= 35:
        return "E"
    else:
        return "F"


def show_report_card(s):
    print("=========== REPORT CARD ===========")
    print("Student :", s["name"])
    print("------------------------------------")
    print("Subject          Marks")
    for i in range(len(SUBJECTS)):
        print(f"{SUBJECTS[i]:<15} {s['marks'][i]:>6g}")
    print("------------------------------------")
    print(f"Total      : {s['total']:g} / {len(SUBJECTS) * 100}")
    print(f"Average    : {s['percent']:.2f}")
    print(f"Percentage : {s['percent']:.2f}%")
    print("Grade      :", s["grade"])
    print("Result     :", s["result"])
    print("====================================")


def add_student():
    name = get_name("Student name: ")
    marks = []
    for subject in SUBJECTS:
        mark = get_float("Marks for " + subject + " (0-100): ",
                         "Marks must be between 0 and 100.", 0, 100, True)
        marks.append(mark)
    total = sum(marks)
    percent = total / len(SUBJECTS)
    result = "PASS"
    for mark in marks:
        if mark < PASS_MARK:
            result = "FAIL"
    student = {"name": name, "marks": marks, "total": total, "percent": percent,
               "grade": get_grade(round(percent, 2)), "result": result}
    students.append(student)
    show_report_card(student)


def view_report_cards():
    if len(students) == 0:
        print("No records available.")
        return
    for s in students:
        show_report_card(s)


def class_summary():
    if len(students) == 0:
        print("No records available.")
        return
    sum_percent = 0
    passed = 0
    topper = students[0]
    for s in students:
        sum_percent = sum_percent + s["percent"]
        if s["result"] == "PASS":
            passed = passed + 1
        if s["percent"] > topper["percent"]:
            topper = s
    print("Students      :", len(students))
    print(f"Class average : {sum_percent / len(students):.2f}%")
    print(f"Topper        : {topper['name']} ({topper['percent']:.2f}%)")
    print("Pass count    :", passed)
    print("Fail count    :", len(students) - passed)


def grading_menu():
    while True:
        print("\n--- GRADING SYSTEM ---")
        print(" 1. Add Student and Marks")
        print(" 2. View All Report Cards")
        print(" 3. Class Summary")
        print(" 4. Back")
        choice = get_int("Enter your choice (1-4): ", 1, 4, "Invalid choice. Enter 1-4.")
        if choice == 1:
            add_student()
        elif choice == 2:
            view_report_cards()
        elif choice == 3:
            class_summary()
        else:
            return


# ---------------- BILLING MODULE ----------------
def get_discount_rate(subtotal):
    if subtotal >= 10000:
        return 0.15
    elif subtotal >= 5000:
        return 0.10
    elif subtotal >= 1000:
        return 0.05
    else:
        return 0


def create_bill():
    customer = get_name("Customer name: ")
    bill_number = "B-" + str(len(bills) + 1).zfill(4)
    print("Bill number:", bill_number)

    item_names = []
    item_prices = []
    item_quantities = []
    while True:
        item_name = get_text("Item name (type 'done' to finish): ", "Item name cannot be empty.")
        if item_name.lower() == "done":
            break
        price = get_float("Unit price: ", "Price must be greater than 0.", 0, 1000000, False)
        quantity = get_int("Quantity: ", 1, 100000, "Quantity must be a whole number >= 1.")
        item_names.append(item_name)
        item_prices.append(price)
        item_quantities.append(quantity)

    if len(item_names) == 0:
        print("No items added. Bill cancelled.")
        return

    subtotal = 0
    for i in range(len(item_names)):
        subtotal = subtotal + item_prices[i] * item_quantities[i]
    rate = get_discount_rate(subtotal)
    discount = round(subtotal * rate, 2)
    taxable = round(subtotal - discount, 2)
    tax = round(taxable * TAX_RATE, 2)
    grand_total = round(taxable + tax, 2)

    print("\n=============== INVOICE ===============")
    print("Bill No  :", bill_number)
    print("Customer :", customer)
    print("---------------------------------------")
    print("Item              Price  Qty      Total")
    for i in range(len(item_names)):
        line_total = item_prices[i] * item_quantities[i]
        print(f"{item_names[i]:<15} {item_prices[i]:>7.2f} {item_quantities[i]:>4} {line_total:>10.2f}")
    print("---------------------------------------")
    print(f"{'Subtotal':<27} {subtotal:>11.2f}")
    print(f"{'Discount (' + str(int(rate * 100)) + '%)':<27} {-discount:>11.2f}")
    print(f"{'Taxable amount':<27} {taxable:>11.2f}")
    print(f"{'Tax (18%)':<27} {tax:>11.2f}")
    print("---------------------------------------")
    print(f"{'GRAND TOTAL':<27} {grand_total:>11.2f}")
    print("=======================================")
    print("Thank you for your purchase!")

    bill = {"number": bill_number, "customer": customer, "grand_total": grand_total}
    bills.append(bill)


def view_bills():
    if len(bills) == 0:
        print("No records available.")
        return
    print("Bill No   Customer              Grand Total")
    print("--------------------------------------------")
    total = 0
    for b in bills:
        print(f"{b['number']:<9} {b['customer']:<20} {b['grand_total']:>12.2f}")
        total = total + b["grand_total"]
    print("--------------------------------------------")
    print(f"{'TOTAL BILLED':<30} {total:>12.2f}")


def billing_menu():
    while True:
        print("\n--- BILLING SYSTEM ---")
        print(" 1. Create New Bill")
        print(" 2. View All Bills")
        print(" 3. Back")
        choice = get_int("Enter your choice (1-3): ", 1, 3, "Invalid choice. Enter 1-3.")
        if choice == 1:
            create_bill()
        elif choice == 2:
            view_bills()
        else:
            return


# ---------------- REPORTS MODULE ----------------
def reports_menu():
    while True:
        print("\n--- VIEW REPORTS ---")
        print(" 1. Expense Report")
        print(" 2. Attendance Report")
        print(" 3. Grading Report")
        print(" 4. Billing Report")
        print(" 5. Back")
        choice = get_int("Enter your choice (1-5): ", 1, 5, "Invalid choice. Enter 1-5.")
        if choice == 1:
            view_expenses()
            if len(expenses) > 0:
                print()
                expense_summary()
        elif choice == 2:
            view_attendance()
            if len(people) > 0:
                print()
                attendance_summary()
        elif choice == 3:
            class_summary()
        elif choice == 4:
            view_bills()
        else:
            return


# ---------------- MAIN MENU ----------------
def display_menu():
    print("=" * 46)
    print("  EXPENSE | ATTENDANCE | GRADING | BILLING")
    print("=" * 46)
    print(" 1. Expense Management")
    print(" 2. Attendance Management")
    print(" 3. Grading System")
    print(" 4. Billing System")
    print(" 5. View Reports")
    print(" 6. Exit")
    print("-" * 46)


def main():
    while True:
        display_menu()
        choice = get_int("Enter your choice (1-6): ", 1, 6, "Invalid choice. Enter 1-6.")
        if choice == 1:
            expense_menu()
        elif choice == 2:
            attendance_menu()
        elif choice == 3:
            grading_menu()
        elif choice == 4:
            billing_menu()
        elif choice == 5:
            reports_menu()
        else:
            break
    print("Thank you for using the system. Goodbye!")


main()