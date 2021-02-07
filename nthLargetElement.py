##To find the nth largest element in a given list
input1 = [9,3,2,5,3,1,1,7,9,6,5] #sample input.
num = 20 #nth element
list1 = list(set(input1))
list1.sort()
if len(list1) < num:
    print(-1)
else:
    print(list1[len(list1)-num])