# #WAP to accept values in 2 DDAs of size 4 * 2 and perfrom addition

import numpy as np

a = []
print("Enter values for first DDA:")

for i in range(4):
    row = []
    for j in range(2):
        n = int(input("Enter number: "))
        row.append(n)
    a.append(row)

b = []
print("Enter values for second DDA:")

for i in range(4):
    row = []
    for j in range(2):
        n = int(input("Enter number: "))
        row.append(n)
    b.append(row)

a = np.array(a)
b = np.array(b)

c = a + b

print("Addition:")
print(c)