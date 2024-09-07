# Find highest value number in given array

arr = [10, 5, 20, 6]
# print(len(arr))  is 4
# print(arr[1])  is '5'
for i in range(0, len(arr)-1):
    if arr[i] > arr[i+1]:
        MaxNum=arr[i]
    else:
        MaxNum=arr[i+1]
print('Maximum Number in array is: ', MaxNum)