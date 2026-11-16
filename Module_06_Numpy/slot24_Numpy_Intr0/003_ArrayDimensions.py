#wap to accept multiple values in list and store in 1-D array and display
import numpy as np
size=int(input("Enter size of array: "))
ls=[]
for i in range(size):
     no=int(input("Enter Number: "))
     ls.append(no)


print(np.array(ls))



