input1 = [1,2,3,4,5,6,7,8,9]
num = 4
res = (sum(input1[len(input1)-num-1:len(input1)-1])-sum(input1[len(input1)-num:]))/num
if res < 0:
    print(res*-1)
else:
    print(res)
