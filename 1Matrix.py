#Create a nXn matrix with the below pattern
#n=5
#[1,1,1,1,1]
#[0,0,0,1,0]
#[0,0,1,0,0]
#[0,1,0,0,0]
#[1,1,1,1,1]
#n=3
#[1,1,1]
#[0,1,0]
#[1,1,1]
import numpy as np
n = 5
arr = np.ones([n,n])
for i in range(1,n-1):
    for j in range(n):
        if i+j != n-1:
            arr[i][j] = 0
l = []
for i in range(n):
    for j in range(n):
        l.append(int(arr[i][j]))
print(arr) #to print the matrix
