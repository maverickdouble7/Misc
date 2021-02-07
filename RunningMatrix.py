##TODO
#to create a matrix of the below form
#4
#4444444
#4333334
#4322234
#4321234
#4322234
#4333334
#4444444
#3
#33333
#32223
#32123
#32223
#33333
import numpy as np
def runningMat( n, f):
    t = n*2-1
    print(t,n,f)
    if n == 1:
        arr[0] = 1
        return
    for i in range(f,t):
        for j in range(f,t):
            if (i in range(f,t) and j == f) or (j == t - 1) or (j == f) or (i == f) or (i == t - 1):
                arr[i][j] = n
    return runningMat(n-1,f+1)
n = 4
t = n*2-1
arr = np.arange(t**2).reshape(t,t)

runningMat(n,0)
print(arr)
