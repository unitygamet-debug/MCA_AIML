#WAP to accept name and roll number form the user and store it in a file called mydata.txt using formatted string crate a statement {my  name is}
print("Enter your name:")
name = input()
print("Enter your Roll no:")
roll = input()
f_string=f"My name is {name} and my roll is  {roll}"

with open("mydata.txt","w") as f:
    f.write(f_string)



with open("mydata.txt","r") as f:
    content = f.read()
    print(content)
