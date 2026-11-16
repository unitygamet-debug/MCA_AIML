#Secure Employee Account Management System
users={}
n=int(input("Enter no. of users:"))
acc_no=1
confrim_pass=0
entered_passright=False

for i in range(n):

    username=input("Enter Username of Account No:")
    enterd_passright=False
    while entered_passright==False:
        password=input("Enter Password of Account No:")
        len_right=False
        is_Upper = False
        is_lower = False
        is_special=False
        is_digit = False
        has_space=True
        if len(password)>8:
            len_right=True
        for i in password:
            if i.isupper():
                is_Upper=True
            if i in "@#$%&*!":
                is_special=True
            if i.isdigit():
                is_digit=True
            if i.islower():
                is_lower=True
            if i.isspace():
                has_space=True
        if len_right==True and is_Upper==True and  is_special==True and is_digit==True and is_lower==True and has_space==False:
            print("Password is valid for ")
            while(True):
                re_pass=input(print("Re-enter Password for "))
                if re_pass==password:
                    print("Password has saved in Database:")
                    users[username]=password
                    break
            enterd_passright=True
            acc_no+=1
        else:
            print(f"Password is not valid for ",{acc_no}, "Please enter valid password:")






