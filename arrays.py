
# pip install numpy


import numpy as np
arr = np.array([10,20,30])
arr1 = np.array([[10,20,30],[20,30,40]])
arr2 = np.array([[10,20,30],[20,30,40],[60,70,80]])
zero = np.zeros((3,4))
ones = np.ones((3,4))
# print(ones)
# print(zero)
# print(arr2)

# eye = np.eye(3)
# print(eye)

# print(arr2[:,1])
print(arr2[0:3,1:3])
# index

print(arr[arr>30])

# pandas
