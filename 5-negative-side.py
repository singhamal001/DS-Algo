# Move all negative numbers to beginning and positive to end with constant extra space
# An array contains both positive and negative numbers in random order.
# Rearrange the array elements so that all negative numbers appear before all positive numbers.

test_arr=[]
n=int(input("Enter the number of elements in the array \n"))
for i in range(0,n):
    test_arr.append(int(input()))

def negative_side(arr):
    for i in range(0, len(arr)):
        if arr[i]<0:
            temp=arr[i]
            arr.remove(arr[i])
            arr.insert(0,temp)
    return arr

print(negative_side(test_arr))
