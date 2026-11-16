#Debug the common errors

#error 1 : variable not define
print(score) #NameError (using a variable before defining it)

#error 2: forgetting quotes
name = Arpita # NameError (it is a string but not in double quotes)

#error 3:(conceptual trap) : number stored as string
age = "19"
print(type(age))