Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


n=int(input("Enter the length of Array1 \n"))

test_arr=[]
print("Enter the elements of Array")
for i in range(0,n):
    test_arr.append(int(input()))

def maxSum(arr):
    sum=0
    for i in range(0,len(arr)):
        if arr[i]>=0:
            sum+=arr[i]
    return sum

print(maxSum(test_arr))
