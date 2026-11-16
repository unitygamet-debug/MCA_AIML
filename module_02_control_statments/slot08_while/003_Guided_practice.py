#complete: keep asking for the password until it matches"python123"
'''correct_password="python123"
entered =""
while entered!=correct_password:
    entered=input("Enter your password: ")
    if entered!=correct_password:
        print("wrong password")
print("access granted")'''


i=0
correct_password="python123"
entered =""
while entered!=correct_password:
    entered=input("Enter your password: ")
    if entered!=correct_password:
        i += 1
        print("wrong password,",5-i,"attempts left")
        if(i==5):
           break

        #how to grnt access grant


