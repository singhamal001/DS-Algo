# Given an array, rotate the array by one position in clock-wise direction.

n=int(input("Enter the length of Array1 \n"))

test_arr=[]
print("Enter the elements of Array")
for i in range(0,n):
    test_arr.append(int(input()))

print(test_arr[len(test_arr)-1], end=" ")
for i in range (0,len(test_arr)-1):
    print(test_arr[i], end=" ")
