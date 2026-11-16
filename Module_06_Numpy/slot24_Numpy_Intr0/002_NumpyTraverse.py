import numpy as np
number_list=[12,45,5.6,45]
arr=np.array(number_list)
result_list=[]
for num in number_list:
    result_list.append(num*2)



print(result_list)
print(type(result_list))

result_arr=arr*2
print(result_arr)
print(type(result_arr))