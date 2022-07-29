#This is the code for sorting an array containing only 0,1 and 2. Without using any sorting algorithm
def sort_012(arr):
    zero=0
    one=0
    two=0
    x=len(arr)
    for i in range(0,x-1):
        if arr[i]==0:
            zero+=1
        elif arr[i]==1:
            one+=1
        else:
            two+=1
    
    for i in range(0,x):
        if i<zero:
            arr[i]=0
        elif i>=zero and i<=zero+one:
            arr[i]=1
        else:
            arr[i]=2
    
    return arr

n=int(input("Enter the number of elements in the array \n"))
test_arr=[]
for i in range(0,n):
    test_arr.append(int(input()))

print(sort_012(test_arr))
