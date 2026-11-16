#WAP to assign values in a DDA of size 3 × 4 and whenever there is an even number, add 3 to it to make it an odd number; also, if the number is odd, add 5 to make it an even number.

import numpy as np
a = []

for i in range(3):
    row = []
    for j in range(4):
        n = int(input("Enter number: "))
        if n % 2 == 0:
            n = n + 3
        else:
            n = n + 5
        row.append(n)
    a.append(row)
a = np.array(a)

print("DDA:")
print(a)