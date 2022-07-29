Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


n=int(input("Enter the length of Array1 \n"))

test_arr=[]
print("Enter the elements of Array")
for i in range(0,n):
    test_arr.append(int(input()))

def maxSum(arr):
    cur_sum = 0
        max_sum = arr[0]
        for i in range(0,len(arr)):
            cur_sum = cur_sum + arr[i]
            if(max_sum<cur_sum):
                max_sum = cur_sum
            if(cur_sum<0):
                cur_sum =0
        return max_sum

print(maxSum(test_arr))
