#Broken : forget to convert before multiplication
price = input("Enter your price: ")
quantity = input("Enter your quantity: ")
#total = price * quantity #TypeError - is result : str

#Fixed
total = int(price) + int(quantity)
print("total: ", total)
