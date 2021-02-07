import math
M1 = [3,2,0]
M2 = [3,9,0]
M1R = M1[0]
M1X = M1[1]
M1Y = M1[2]
M2R = M2[0]
M2X = M2[1]
M2Y = M2[2]
if math.sqrt((M2X-M1X)**2+(M2Y-M1Y)**2) >= (M1R+M2R):
    print(math.sqrt((M2X-M1X)**2+(M2Y-M1Y)**2))
    print('Collision')
else:
    print('No Collision')
