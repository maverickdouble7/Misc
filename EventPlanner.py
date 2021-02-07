import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
intervals = input_list[0]
date = input_list[1]
count = 0
for i in intervals:
    if date >= i[0] and date <= i[1]:
        count = count+1
print(count)
