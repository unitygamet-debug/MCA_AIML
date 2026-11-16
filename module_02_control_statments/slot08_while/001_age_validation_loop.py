#wap age from the user and check the user eligible to vote or not
age = int(input("what is your age: "))

'''if age>0 and age<=130:
  if age>=18:
    print("you are eligible to vote")
  else:
    print("you are not eligible to vote")
else:
    print("this is not a human valid age")'''

'''while True:
    age = int(input("what is your age: "))

    if age>0 and age<=130:
        if age>=18:
            print("you are eligible to vote\n")
        else:
            print("you are not eligible to vote\n")
    else:
        print("this is not a human valid age\n")'''

while True:
    age = int(input("what is your age: "))

    if age > 0 and age <= 130:
        if age >= 18:
            print("you are eligible to vote\n")
        else:
            print("you are not eligible to vote\n")
    else:
       break

