'''
This program will create an array containing the values 1–15, reshape it
into a 3-by-5 array, then use indexing and slicing techniques and then display the following outputs
Author: Hafsa Aman
Homework #2 Question 1
'''

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
newarr = arr.reshape(3, 5)
print(newarr)

print(newarr[2])
print()
print(newarr[2,:])
print()
print(newarr[:,3])
print()
print(newarr[[0,1],:])
print()
print(newarr[:,2:5])
print()
print(newarr[1,4])
print()
print(newarr[1:3,[0,2,4]])

