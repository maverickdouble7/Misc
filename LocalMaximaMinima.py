#Reading the input
input_str = [12, 18, 11, 24, 55]

maxi = [input_str[i+1] for i in range(0,len(input_str)-2) if input_str[i+1] > input_str[i] and input_str[i+1]>input_str[i+2] ]
mini = [input_str[i+1] for i in range(0,len(input_str)-2) if input_str[i+1] < input_str[i] and input_str[i+1]<input_str[i+2] ]
if input_str[0] > input_str[1]:
    maxi = [input_str[0]] + maxi
else:
    mini = [input_str[0]] + mini
if input_str[len(input_str)-1] < input_str[len(input_str)-2]:
    mini = mini + [input_str[len(input_str)-1]]
else:
    maxi = maxi + [input_str[len(input_str)-1]]
print(maxi)
print(mini)