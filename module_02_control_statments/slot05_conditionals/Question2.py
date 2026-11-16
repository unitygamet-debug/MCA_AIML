#wap to accept monthly salary and check the user eligible for tax or not tax only applicable if annual salary is more than the threshold
mon_salary=int(input("enter your  monthly salary:"))
ann = mon_salary*12
print("annual salary:",ann)

if ann> 500000:
    print("Eligible for tax")
else:
    print(" not eligible for tax")

#wap to accept quantity and price of laptop sold by a sale person where companies based on
#if sale person are sale of 100000>10% commission
#if sale is more than 17000less than 70000>7%commission
#if sale 40000>70000
# if sale less than 40000 than no commission

quantity = int(input("Enter quantity of laptops sold: "))
price = float(input("Enter price of one laptop: "))

sale = quantity * price

print("Total Sale =", sale)

if sale >= 100000:
    commission = sale * 10 / 100
elif sale >= 70000:
    commission = sale * 7 / 100
elif sale >= 40000:
    commission = 0
else:
    commission = 0

print("Commission =", commission)
