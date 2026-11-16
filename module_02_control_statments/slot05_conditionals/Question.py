#wap ]to accept the mark of three sub and find the total avg

math=int(input("enter maths number"))
science=int(input("enter science number"))
python=int(input("enter python number"))

avg=(math+science+python)/3

if (math>=80 ):
    print("you are eligible")
elif(science>=80):
    print("you are eligible")
elif(python>=80):
    print("you are eligible")
else:
    print("you are not eligible")