# Given an array arr[] and an integer K where K is smaller than size of array,
# the task is to find the Kth smallest element in the given array.
# It is given that all array elements are distinct.
#Taking Input for the array
test_arr=[]
length=int(input("Please enter the length of the Array \n"))
for i in range(0,length):
    inp=input()
    test_arr.append(inp)

print(test_arr)
test_arr.sort()
n=int(input("Give the K element \n"))
print(test_arr[n-1])
