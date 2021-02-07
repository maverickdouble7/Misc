string = '(){}][' ##Sample input
open = ['(','[','{']
count = 0
for i in string:
    if i in open:
        count = count + 1
    else:
        count = count - 1
if count == 0:
    print('balanced')
else:
    print('not balanced')

##Second solution
string=input()
prth = ['()', '{}', '[]'] #all parenthesis
while any(x in string for x in prth):
    for pr in prth:
        string = string.replace(pr, '')
if string:
    print("not balanced")
else:
    print("balanced")