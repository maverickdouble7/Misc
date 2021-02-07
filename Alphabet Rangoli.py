import numpy as np
import pandas as pd
import string
alispha = string.ascii_lowercase
n = 5 #Change here for more
lis = [ ]
for i in range(n):
    s = "-".join(alispha[i:n])
    lis.append((s[::-1]+s[1:]).center(4*n-3, "-"))
for i in range(len(lis)-1,0,-1):
    print(lis[i])
for i in range(len(lis)):
    print(lis[i])