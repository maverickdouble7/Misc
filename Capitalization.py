import numpy as np
import pandas as pd

S = input()
s = S.split(' ')
j = []
for i in s:
    j.append(i.capitalize())
print(' '.join(j))
