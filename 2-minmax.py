#Code to find minimum and maximum in an array with the help of for-loop

def minmax(arr):
    n=len(arr)

    if n==1:
        min=arr[0]
        max=arr[0]
    elif n==2:
        if arr[0]>arr[1]:
            min=arr[1]
            max=arr[0]
        else:
            max=arr[1]
            min=arr[0]
    else:
        min=arr[0]
        max=arr[0]
        for i in range(0,n):
            if arr[i]>max:
                max=arr[i]
            if arr[i]<min:
                min=arr[i]
    
    return min, max

test_arr=[1,23,4,5,6,8]
print(test_arr)
print(minmax(test_arr))
